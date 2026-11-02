import hashlib
import json
import subprocess
import tarfile
import urllib.request
from pathlib import Path

BASE = "https://github.com/safeney/Tavchain/releases/download/docker-771002-1/"
ARCHIVE = "tavchain-docker-771002-1-linux-amd64.tar.gz"
ARCHIVE_SHA = "396583bf97f855552e69424c79628fd09ce7a9678f456302f9b422bc96a08c40"
MANIFEST_SHA = "65f6fe0fe3ad0aa53d0719fef2dd9f26a09b533b6139bd2f05e10ddf408e6cb0"
FINGERPRINT = "SHA256:rZRDFiztp0bd51gCAI/qKBGxkOKl9Fv52UWdbUpUQRM"

def digest(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()

def extract(archive, destination):
    assert digest(archive) == ARCHIVE_SHA, "Released archive hash mismatch"
    with tarfile.open(archive) as bundle:
        seen = set()
        for member in bundle:
            path = Path(member.name)
            assert not path.is_absolute() and ".." not in path.parts
            assert path.parts[0] == "tavchain-docker-771002-1"
            assert member.isfile() or member.isdir()
            assert member.name not in seen
            seen.add(member.name)
        bundle.extractall(destination, filter="data")

def main():
    work = Path(".container-release")
    work.mkdir(exist_ok=False)
    for name in [ARCHIVE, "DOCKER-RELEASE.json", "DOCKER-RELEASE.json.sig", "release1_ed25519.pub"]:
        with urllib.request.urlopen(BASE + name, timeout=60) as source, (work / name).open("xb") as target:
            while chunk := source.read(1024 * 1024):
                target.write(chunk)
    assert digest(work / "DOCKER-RELEASE.json") == MANIFEST_SHA
    fingerprint = subprocess.check_output(["ssh-keygen", "-lf", str(work / "release1_ed25519.pub")], text=True)
    assert FINGERPRINT in fingerprint
    allowed = work / "allowed_signers"
    allowed.write_text("safeney-tavchain-releases " + (work / "release1_ed25519.pub").read_text())
    subprocess.run(["ssh-keygen", "-Y", "verify", "-f", str(allowed), "-I", "safeney-tavchain-releases",
                    "-n", "tavchain-release-v1", "-s", str(work / "DOCKER-RELEASE.json.sig")],
                   input=(work / "DOCKER-RELEASE.json").read_bytes(), check=True)
    extract(work / ARCHIVE, work)
    package = work / "tavchain-docker-771002-1"
    subprocess.run(["sha256sum", "--check", "SHA256SUMS"], cwd=package, check=True)
    assert digest(package / "bin/tavchaind") == "fa434051778f277ba03454dde427aa2ec431a93a010b7ded3746edde50bb4991"
    assert digest(package / "network/genesis.json") == "a101ab9ccf1478757af8a69d832548ea1167e552fe6d6ef6621a77447a54e924"
    print(json.dumps({"archive_verified": True, "existing_signature_verified": True}))

if __name__ == "__main__":
    main()
