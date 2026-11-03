# Tavchain Testnet 771002

| Setting | Value |
| --- | --- |
| Native chain ID | tavchaintestnet_771002-1 |
| EVM chain ID | 771002 (0xbc3ba) |
| Public EVM RPC | https://api.testnet.tavchain.safeney.com/ |
| Explorer | https://explorer.tavchain.safeney.com/ |
| Asset | Test Tavcoin / TAV, 18 decimals, atav base units |
| Deployed validator client | 1.8.1-tavchain.eval1 |
| Native full-node downloads | 1.8.1-tavchain.eval1-native1 |
| Genesis SHA-256 | a101ab9ccf1478757af8a69d832548ea1167e552fe6d6ef6621a77447a54e924 |
| Deployed validator binary SHA-256 | fa434051778f277ba03454dde427aa2ec431a93a010b7ded3746edde50bb4991 |

Use the genesis and peers in [networks/tavchaintestnet_771002-1/](networks/tavchaintestnet_771002-1/).

Authenticate network files using the [signed network release](https://testnet.tavchain.safeney.com/downloads/tavchain-network-771002-1/VERIFY.md), rather than trusting a checksum copied into a README alone.

The 771001-1 and 771001-2 networks are retired. Their balances, nonces and contracts did not carry forward. The original node-release directory includes retired network settings; use its binary/source authentication with the separate 771002 network package. Never silently replace a signed file or combine an old genesis with current instructions.

For a new full node, choose the [ready-to-run native bundle](https://github.com/safeney/Tavchain/releases/tag/native-bundle-771002-1) for Linux x86-64, Linux ARM64 or Windows x86-64, or the [prebuilt Docker image](https://docs.tavchain.safeney.com/tavchain/operate/node-docker) for Linux x86-64. Both include the current network configuration. Authenticate a native bundle using its BUNDLE-RELEASE.json, detached signature and VERIFY.md before running its launcher. Platform support is scoped to the tested non-validator environments described in the [native guide](https://docs.tavchain.safeney.com/tavchain/operate/node-native).

The [earlier native client archives](https://github.com/safeney/Tavchain/releases/tag/native-1.8.1-tavchain.eval1-native1) remain available. Those archives contain executables without genesis and require the separately authenticated 771002 network package.

The network configuration is independent of the source code's default/example chain settings. Start with the [installation chooser](https://docs.tavchain.safeney.com/tavchain/operate) for the matching home, ports and synchronization checks. The [earlier manual Linux guide](https://docs.tavchain.safeney.com/tavchain/operate/run-full-node) remains available for its separate client package.
