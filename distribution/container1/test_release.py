import importlib.util
import io
import tarfile
import tempfile
import unittest
import urllib.error
from io import BytesIO
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parent
def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / (name + ".py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
prepare = load("prepare")
accept = load("accept")
publish = load("publish")

class ReleaseChecks(unittest.TestCase):
    def test_matching_block(self):
        block = {k: k for k in ["hash", "stateRoot", "receiptsRoot", "transactionsRoot"]}
        accept.compare_block(block, block.copy())

    def test_each_block_field_mismatch_is_rejected(self):
        block = {k: k for k in ["hash", "stateRoot", "receiptsRoot", "transactionsRoot"]}
        for key in block:
            with self.subTest(field=key), self.assertRaises(AssertionError):
                accept.compare_block({**block, key: "wrong"}, block)

    def test_missing_block_is_rejected(self):
        with self.assertRaises(AssertionError):
            accept.compare_block(None, {})

    def test_archive_hash_mismatch_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            archive = Path(tmp) / "input.tar"
            archive.write_bytes(b"bad")
            with self.assertRaises(AssertionError):
                prepare.extract(archive, Path(tmp) / "out")

    def test_archive_traversal_and_links_are_rejected(self):
        for name, kind in [("../outside", tarfile.REGTYPE),
                           ("tavchain-docker-771002-1/link", tarfile.SYMTYPE),
                           ("other/file", tarfile.REGTYPE)]:
            with self.subTest(name=name), tempfile.TemporaryDirectory() as tmp:
                archive = Path(tmp) / "input.tar"
                with tarfile.open(archive, "w") as bundle:
                    member = tarfile.TarInfo(name)
                    member.type = kind
                    member.linkname = "/etc/passwd" if kind == tarfile.SYMTYPE else ""
                    member.size = 0
                    bundle.addfile(member, io.BytesIO(b""))
                with patch.object(prepare, "ARCHIVE_SHA", prepare.digest(archive)):
                    with self.assertRaises(AssertionError):
                        prepare.extract(archive, Path(tmp) / "out")

    def test_registry_404_allows_new_package(self):
        error = urllib.error.HTTPError("https://api.github.com/", 404, "missing", {}, BytesIO())
        with patch.object(publish.urllib.request, "urlopen", side_effect=error):
            publish.require_new_package("synthetic-not-a-token")

    def test_registry_auth_and_server_failures_stop_publication(self):
        for code in [401, 403, 429, 500]:
            error = urllib.error.HTTPError("https://api.github.com/", code, "failure", {}, BytesIO())
            with self.subTest(code=code), patch.object(publish.urllib.request, "urlopen", side_effect=error):
                with self.assertRaises(urllib.error.HTTPError):
                    publish.require_new_package("synthetic-not-a-token")

    def test_existing_registry_package_stops_publication(self):
        with patch.object(publish.urllib.request, "urlopen") as request:
            request.return_value.__enter__.return_value.status = 200
            with self.assertRaises(RuntimeError):
                publish.require_new_package("synthetic-not-a-token")

    def test_candidate_uses_standard_public_runner_and_manual_trigger(self):
        workflow = (ROOT.parents[1] / ".github/workflows/container-release1.yml").read_text()
        self.assertIn("workflow_dispatch:", workflow)
        self.assertIn("runs-on: ubuntu-24.04", workflow)
        self.assertNotIn("pull_request:", workflow)
        self.assertNotIn("timeout-minutes:", workflow)
        self.assertNotIn("upload-artifact", workflow)
        self.assertLess(workflow.index("Accept disposable non-validator"), workflow.index("Publish accepted image"))

if __name__ == "__main__":
    unittest.main()
