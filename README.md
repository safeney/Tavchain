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

Use the [native installation guide](https://docs.tavchain.safeney.com/tavchain/operate/node-native) for Linux x86-64, Linux ARM64 and Windows x86-64. Verify the [signed native release manifest](https://testnet.tavchain.safeney.com/downloads/tavchain-native-1.8.1-tavchain.eval1-native1/NATIVE-RELEASE.json) and its detached signature before extracting or running a download. The guide includes the trusted release-key fingerprint, platform commands and the separate authenticated 771002 network configuration.

These clients passed non-validator synchronization, fixed-height state comparisons, graceful shutdown and same-identity restart on their tested environments. macOS and Windows ARM64 binaries are not provided. The [Docker package](https://docs.tavchain.safeney.com/tavchain/operate/node-docker) remains a separate Linux amd64 release.

The native download directory also contains the exact source archive, packaging patch, build instructions and runtime notices. Its four packaging changes are separate from the earlier source snapshot under `node/`. Downloading this release does not upgrade running validators.

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
