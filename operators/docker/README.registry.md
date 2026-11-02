# Run a Tavchain node with the published image

Candidate guide: the registry image has not been built, accepted or published yet.

For Linux x86-64 with Docker Engine and Compose installed:

```sh
git clone --depth 1 https://github.com/safeney/Tavchain.git
cd Tavchain/operators/docker
docker compose -f compose.registry.yaml run --rm init
docker compose -f compose.registry.yaml up -d node
```

The image includes the client and Tavchain Testnet configuration. Initialization creates a new non-validator node identity in a named volume. No wallet, token balance, manual genesis download or local image build is required.

Check progress:
```sh
docker compose -f compose.registry.yaml logs --tail 100 node
```

Stop and resume:
```sh
docker compose -f compose.registry.yaml stop node
docker compose -f compose.registry.yaml up -d node
```

Keep the same directory/project and volume. Initialize once; ordinary stops preserve data. Do not use `down --volumes` on retained node data. Local RPC ports bind to 127.0.0.1. The image is for a Linux amd64 non-validator; other host/validator configurations are separate.

The final guide will record the accepted registry digest. Set TAVCHAIN_IMAGE to the full image@sha256 digest to pin exact image bytes. The existing archive and local-build Compose file remain available. Registry authentication and its digest record do not claim a new detached release-key signature.
