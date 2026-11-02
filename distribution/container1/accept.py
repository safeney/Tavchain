import base64
import hashlib
import json
import os
import subprocess
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COMPOSE = ROOT / "operators/docker/compose.registry.yaml"
PUBLIC = "https://api.testnet.tavchain.safeney.com/"
PROJECT = "tavchain-registry-accept1"
CHAIN = "tavchaintestnet_771002-1"

def compose(*args, check=True):
    return subprocess.run(["docker", "compose", "-p", PROJECT, "-f", str(COMPOSE), *args],
                          text=True, capture_output=True, check=check)

def rpc(url, method, params=None):
    request = urllib.request.Request(url, data=json.dumps(
        {"jsonrpc": "2.0", "id": 1, "method": method, "params": params or []}).encode(),
        headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(request, timeout=20) as response:
        value = json.load(response)
    assert "error" not in value, "RPC returned an error"
    return value["result"]

def native(path):
    with urllib.request.urlopen("http://127.0.0.1:29657/" + path, timeout=20) as response:
        value = json.load(response)
    assert "error" not in value
    return value["result"]

def container_state():
    ids = compose("ps", "--all", "--quiet", "node").stdout.split()
    assert len(ids) == 1
    container = json.loads(subprocess.check_output(["docker", "inspect", ids[0]]))[0]
    assert container["RestartCount"] == 0, "Trial process restarted unexpectedly"
    return container["State"]

def wait_sync(identity=None):
    while True:
        state = container_state()
        assert state["Running"] and not state["OOMKilled"], "Trial container stopped"
        try:
            status = native("status")
        except (urllib.error.URLError, TimeoutError, ConnectionError):
            time.sleep(2)
            continue
        assert status["node_info"]["network"] == CHAIN
        assert int(status["validator_info"]["voting_power"]) == 0
        if identity:
            assert status["node_info"]["id"] == identity
        height = int(status["sync_info"]["latest_block_height"])
        reference = int(rpc(PUBLIC, "eth_blockNumber"), 16)
        print(json.dumps({"phase": "sync", "height": height, "public_height": reference}), flush=True)
        if not status["sync_info"]["catching_up"] and height >= reference - 1:
            assert int(native("net_info")["n_peers"]) > 0
            assert rpc("http://127.0.0.1:29645/", "eth_chainId") == rpc(PUBLIC, "eth_chainId") == "0xbc3ba"
            return status
        time.sleep(10)

def compare_block(local, reference):
    assert local and reference
    for key in ["hash", "stateRoot", "receiptsRoot", "transactionsRoot"]:
        assert local[key] == reference[key], key

def agreement(height, validators):
    evidence = []
    for h in range(height - 2, height + 1):
        reference = rpc(PUBLIC, "eth_getBlockByNumber", [hex(h), False])
        compare_block(rpc("http://127.0.0.1:29645/", "eth_getBlockByNumber", [hex(h), False]), reference)
        assert "0x" + native("block?height=" + str(h))["block_id"]["hash"].lower() == reference["hash"].lower()
        membership = native("validators?height=" + str(h) + "&per_page=100")["validators"]
        assert {v["address"] for v in membership} == validators
        assert len(membership) == 4 and all(int(v["voting_power"]) > 0 for v in membership)
        for method, params in [
            ("eth_getBalance", ["0xB8A2b51087ABBabbCC46383685cB45cb6A870C24", hex(h)]),
            ("eth_getCode", ["0x9FEE6A0eAf071Dc6fFa1B6193cE1ab52E085F525", hex(h)]),
        ]:
            assert rpc(PUBLIC, method, params) == rpc("http://127.0.0.1:29645/", method, params)
        evidence.append({"height": h, "hash": reference["hash"], "state_root": reference["stateRoot"]})
    return evidence

def stop():
    compose("stop", "node")
    state = container_state()
    assert not state["Running"] and not state["OOMKilled"] and state["ExitCode"] == 0

def run():
    assert os.environ["TAVCHAIN_IMAGE"].startswith("tavchain-registry-candidate:")
    assert not compose("ps", "--all", "--quiet").stdout.strip(), "Trial project already exists"
    volumes = subprocess.check_output(["docker", "volume", "ls", "--filter",
        "label=com.docker.compose.project=" + PROJECT, "--quiet"], text=True)
    assert not volumes.strip(), "Trial volume already exists"
    assert rpc(PUBLIC, "eth_chainId") == "0xbc3ba"
    genesis = json.loads((ROOT / ".container-release/tavchain-docker-771002-1/network/genesis.json").read_text())
    validators = set()
    for tx in genesis["app_state"]["genutil"]["gen_txs"]:
        for msg in tx["body"]["messages"]:
            if msg["@type"] == "/cosmos.staking.v1beta1.MsgCreateValidator":
                validators.add(hashlib.sha256(base64.b64decode(msg["pubkey"]["key"])).digest()[:20].hex().upper())
    assert len(validators) == 4
    success = False
    image = json.loads(subprocess.check_output(["docker", "image", "inspect", os.environ["TAVCHAIN_IMAGE"]]))[0]
    result = {"status": "RUNNING", "phases": [], "image_id": image["Id"]}
    try:
        compose("run", "--rm", "init")
        repeated = compose("run", "--rm", "init", check=False)
        assert repeated.returncode != 0 and "Node data already exists" in repeated.stderr + repeated.stdout
        compose("up", "-d", "node")
        status = wait_sync()
        identity = status["node_info"]["id"]
        height = int(status["sync_info"]["latest_block_height"]) - 1
        result["phases"].append({"phase": "first_sync", "checks": agreement(height, validators)})
        stop()
        while int(rpc(PUBLIC, "eth_blockNumber"), 16) < height + 4:
            time.sleep(2)
        compose("up", "-d", "node")
        status = wait_sync(identity)
        height = int(status["sync_info"]["latest_block_height"]) - 1
        result["phases"].append({"phase": "restart_sync", "checks": agreement(height, validators)})
        stop()
        success = True
        result.update(status="PASS", same_identity=True, zero_voting_power=True)
    finally:
        if success:
            compose("down", "--volumes")
            assert not compose("ps", "--all", "--quiet").stdout.strip()
            assert not subprocess.check_output(["docker", "volume", "ls", "--filter",
                "label=com.docker.compose.project=" + PROJECT, "--quiet"], text=True).strip()
            result["fresh_state_removed"] = True
        else:
            compose("stop", "node", check=False)
            result.update(status="FAIL", retained_until_runner_disposal=True)
        Path("container-acceptance-result.json").write_text(json.dumps(result, indent=2))
    return result

if __name__ == "__main__":
    print(json.dumps(run()))
