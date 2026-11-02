# Tavchain full node with Docker Compose
Tested on Linux amd64 with Docker Engine29.4.1 and Compose5.1.3. Public image-registry distribution is not provided; build this package locally.

This package wraps the released Linux amd64 client. It follows Tavchain Testnet (EVM 771002; native tavchaintestnet_771002-1) without registering a validator or using a wallet. Named Docker storage holds the new node's private identity and ledger. Never mount an existing validator home here.

## Prerequisites
Docker Engine with Compose v2 on a Linux amd64 host, persistent SSD space, accurate time and outbound internet. Desktop/WSL and ARM acceptance are separate. The runtime image contains the tested client and an immutable Debian base; it does not rebuild the node or switch its database backend.

## Build and initialize
From this package directory, use the same project name for every command. Build locally from the included executable and pinned base image.
```sh
docker compose -p tavchain-fullnode build node
docker compose -p tavchain-fullnode run --rm init
docker compose -p tavchain-fullnode up -d node
docker compose -p tavchain-fullnode logs --tail 100 node
```
Initialization refuses any nonempty data directory. If interrupted, retain the volume and inspect it; do not delete/reinitialize it to hide an error. Initialization creates only a new P2P identity and an unused consensus key. It creates no wallet or validator registration.

## Verify sync
```sh
curl --fail --silent --show-error http://127.0.0.1:29657/status
curl --fail --silent --show-error http://127.0.0.1:29645/ -H 'Content-Type: application/json' --data '{"jsonrpc":"2.0","id":1,"method":"eth_chainId","params":[]}'
```
Require native network tavchaintestnet_771002-1, EVM result 0xbc3ba, advancing blocks, peers, catching_up=false and voting_power=0 for this unregistered observer. Compare the same fixed block hash with the public RPC; matching latest heights alone is insufficient. RPC listens on container interfaces for Docker forwarding, but host publications bind only to 127.0.0.1. No P2P port is published; outbound persistent peers support this observer profile.

## Stop, resume and upgrade
```sh
docker compose -p tavchain-fullnode stop node
docker compose -p tavchain-fullnode up -d node
docker compose -p tavchain-fullnode down
```
Ordinary down retains the named volume. Never use down --volumes or volume prune for retained state. Preserve the project name so Docker reuses the same data. Do not initialize again on restart or upgrade.
unless-stopped provides standard container restart behavior while Docker is running. It does not itself enable the host Docker service at boot. Five-minute stop grace gives the database time to close after SIGTERM; it is not a chain expiry or running-time limit.

For an upgrade, stop cleanly and follow that release's compatibility instructions before replacing its image. No general downgrade safety is claimed. Do not run two processes against one data volume.

## What is retained
Current full-history native settings and the authenticated 771002 network files are included. No snapshot restore, pruning, reset, automatic refill, wallet signing, telemetry or expiration is added. Source/dependency archives and notices remain available from the current authenticated node release; the image carries its original notices.

The image is pinned to Linux amd64. Docker Desktop and emulation do not establish native Windows, macOS or ARM acceptance. See https://docs.tavchain.safeney.com/tavchain/operate/run-full-node for native release requirements.
