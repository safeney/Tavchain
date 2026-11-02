# Full-node packaging

The Docker directory contains the original local-build packaging source from the authenticated Tavchain Docker release. The large bin/tavchaind executable is deliberately not stored in Git. For that complete package, use the docker-771002-1 release archive.

Use the [published-image guide](docker/README.registry.md) and compose.registry.yaml to run the accepted prebuilt image without building it locally. The default image is pinned by digest. The existing compose.yaml remains the archive/local-build workflow.

Existing guide: https://docs.tavchain.safeney.com/tavchain/operate/node-docker

The original package README, notices, Apache 2.0 packaging permission and dependency terms remain applicable.
