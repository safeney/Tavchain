import json
import os
import re
import subprocess
import tempfile
import urllib.error
import urllib.request
from pathlib import Path

def require_new_package(token):
    request = urllib.request.Request(
        "https://api.github.com/orgs/safeney/packages/container/tavchain-fullnode",
        headers={"Authorization": "Bearer " + token, "Accept": "application/vnd.github+json",
                 "X-GitHub-Api-Version": "2022-11-28"})
    try:
        with urllib.request.urlopen(request, timeout=30):
            pass
    except urllib.error.HTTPError as error:
        if error.code == 404:
            return
        raise
    raise RuntimeError("Package already exists; review its versions before another publication")

def main():
    token = os.environ["GH_TOKEN"]
    image = os.environ["REGISTRY_IMAGE"]
    candidate = os.environ["TAVCHAIN_IMAGE"]
    assert image == "ghcr.io/safeney/tavchain-fullnode:1.8.1-tavchain.eval1-771002-docker1"
    assert candidate.startswith("tavchain-registry-candidate:")
    result = json.loads(Path("container-acceptance-result.json").read_text())
    assert result["status"] == "PASS" and result["fresh_state_removed"]
    inspect = json.loads(subprocess.check_output(["docker", "image", "inspect", candidate]))[0]
    assert inspect["Id"] == result["image_id"]
    require_new_package(token)
    with tempfile.TemporaryDirectory(prefix="tavchain-registry-auth-", dir=os.environ["RUNNER_TEMP"]) as config:
        env = {**os.environ, "DOCKER_CONFIG": config}
        subprocess.run(["docker", "login", "ghcr.io", "--username", os.environ["GITHUB_ACTOR"],
                        "--password-stdin"], input=token.encode(), env=env, capture_output=True, check=True)
        subprocess.run(["docker", "tag", candidate, image], env=env, check=True)
        subprocess.run(["docker", "push", image], env=env, check=True)
        published = json.loads(subprocess.check_output(["docker", "image", "inspect", image], env=env))[0]
        assert published["Id"] == result["image_id"]
        digests = [v for v in published["RepoDigests"] if re.fullmatch(
            r"ghcr.io/safeney/tavchain-fullnode@sha256:[0-9a-f]{64}", v)]
        assert len(digests) == 1
        with Path(os.environ["GITHUB_STEP_SUMMARY"]).open("a") as summary:
            summary.write("Accepted container digest: " + digests[0] + "\n\n")
            summary.write(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"published_digest": digests[0], "image_id": published["Id"]}))

if __name__ == "__main__":
    main()
