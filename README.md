# Tavchain

Tavchain is an experimental, Cronos-derived EVM blockchain. Tavchain Testnet uses native Cosmos SDK staking and CometBFT consensus. Test TAV has no monetary value.

## Current network

| Setting | Value |
| --- | --- |
| EVM chain ID | `771002` |
| Native chain ID | `tavchaintestnet_771002-1` |
| Deployed validator client | `1.8.1-tavchain.eval1` |
| Native full-node downloads | `1.8.1-tavchain.eval1-native1` (Linux x86-64, Linux ARM64, Windows x86-64) |
| Native asset | Tavcoin (`TAV`), 18 decimals; base denomination `atav` |

- [Documentation](https://docs.tavchain.safeney.com/)
- [Network configuration](NETWORK.md)
- [Connect a wallet](https://docs.tavchain.safeney.com/tavchain/connect)
- [Deploy a contract](https://docs.tavchain.safeney.com/tavchain/write-contract)
- [Run a native full node](https://docs.tavchain.safeney.com/tavchain/operate/node-native)
- [Run a node with Docker](https://docs.tavchain.safeney.com/tavchain/operate/node-docker)
- [Explorer](https://explorer.tavchain.safeney.com/)
- [Faucet](https://faucet.tavchain.safeney.com/)
- [Service status](https://status.tavchain.safeney.com/status/tavchain)
- Support: support@safeney.com

The initial four validators remain under shared administration. The testnet is experimental and unaudited; registration, active validator membership and independently controlled operation are different milestones.

## Downloads

Use the versioned GitHub releases:
- [Native full-node clients](https://github.com/safeney/Tavchain/releases/tag/native-1.8.1-tavchain.eval1-native1): Linux x86-64, Linux ARM64 and Windows x86-64, with exact source and runtime notices.
- [Current network and Hardhat starter](https://github.com/safeney/Tavchain/releases/tag/network-771002-1): authenticated configuration for chain 771002 and the complete starter ZIP.
- [Docker full-node package](https://github.com/safeney/Tavchain/releases/tag/docker-771002-1): complete Linux amd64 archive with the executable, Compose configuration and network files.

These assets mirror the existing published downloads without changing their bytes or signatures. Authenticate the applicable signed manifest using the release-key fingerprint in the [installation guides](https://docs.tavchain.safeney.com/tavchain/operate). The original testnet download URLs remain available. GitHub's automatic source ZIP is not a compiled executable.

For a new Linux x86-64 node, use the [prebuilt image](https://github.com/safeney/Tavchain/pkgs/container/tavchain-fullnode) and [short Compose setup](operators/docker/README.registry.md). The image includes the client and current network configuration; no local image build or separate genesis download is required. The Compose file pins the accepted image by digest.

Browse the complete [Hardhat starter source](examples/hardhat), [Docker packaging source](operators/docker) and [native packaging references](distribution/native1). The original Docker archive and local-build configuration remain available.

Full-node testing does not establish validator-signing support for the native1 platforms. macOS and Windows ARM64 downloads are not available. No running validator is upgraded by this repository update.

## Source layout

- `node/`: the accepted node release source, including its upstream attribution, dependencies manifests, tests and eight Tavchain modifications.
- `networks/tavchaintestnet_771002-1/`: the current public genesis and peer list.

The files in `node/` match the published release-source archive. Its upstream README, documentation, CI examples and source-level network notes are historical Cronos/candidate references. Use the Tavchain documentation and the network files above to join Tavchain Testnet. Nested upstream workflows are not enabled as repository automation.

## Build and verification

Read the release's [build reproduction instructions](https://testnet.tavchain.safeney.com/downloads/tavchain-node-1.8.1-tavchain.eval1/BUILD-RECOMBINE.md) and [release verification instructions](https://testnet.tavchain.safeney.com/downloads/tavchain-node-1.8.1-tavchain.eval1/VERIFY.md). In this repository, `node/` is the source root. Preserve the pinned dependencies, compiler and build flags when reproducing the accepted binary.

The authenticated source package previously reproduced the tested binary. This repository refresh reorganizes those source files; it does not introduce a new binary, consensus change or fresh full-suite test result.

## Security and licensing

Do not commit validator keys, signer state, wallet secrets, keyrings, credentials or databases. Report security issues privately to support@safeney.com.

Node source and the approved Tavchain modifications are distributed under Apache 2.0, with dependency terms and attribution retained. See [node/LICENSE](node/LICENSE), [node/TAVCHAIN-MODIFICATIONS.md](node/TAVCHAIN-MODIFICATIONS.md) and the dependency notices in the published release. This repository contains public node software and public network configuration. Operational credentials and infrastructure administration are maintained separately.
