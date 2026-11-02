#!/bin/sh
set -eu
umask 077
if [ -n "$(find /data -mindepth 1 -maxdepth 1 -print -quit)" ]; then
    echo "Node data already exists. Keep it; do not initialize again." >&2
    exit 1
fi
cd /opt/tavchain/network
sha256sum --check SHA256SUMS
tavchaind init "${TAVCHAIN_MONIKER:-my-tavchain-fullnode}" --chain-id tavchaintestnet_771002-1 --default-denom atav --home /data
cp genesis.json config.toml app.toml /data/config/
echo "Node initialized. Start it with docker compose up -d node."
