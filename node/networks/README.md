# Tavchain network configuration

This candidate builds on Cronos v1.8.1. It is not a deployed network.

`native-asset-metadata.json` is one Cosmos SDK bank Metadata object: Tavcoin/TAV, base denomination `atav`, display denomination `tav`, exponent18. One TAV equals1000000000000000000atav. Include the object in the fresh genesis bank denom_metadata array and select atav for the EVM native denomination when assembling the reviewed genesis. This file is not a complete genesis or an economic allocation.

The CLI is tavchaind, the default node home is .tavchain, environment prefix TAVCHAIND (matching the SDK server executable-name convention), and Cosmos Bech32 account prefix tav. Validator/operator and consensus suffixes follow the SDK defaults. Ethereum-facing accounts retain standard0x20-byte addresses and Ethereum HD coin type60. Address prefixes do not distinguish networks: the Cosmos chain ID and numeric EVM chain ID must do so.

No chain ID is hard-coded into this candidate. Select distinct fresh testnet/mainnet identifiers through the existing upstream genesis/CLI chain-id mechanism; do not reuse Cronos IDs or the historical Tavchain genesis. No public registry allocation is claimed. Testnet uses the same Tavcoin/TAV precision with valueless-token labeling, as other EVM chains distinguish environments through network names and IDs.

The upstream cmd/cronosd source path and Go module/import paths remain unchanged to keep the patch small and upstream updates traceable. make build and make install produce tavchaind. Existing upstream scripts, fixtures, module/store names, Cronos-specific RPC namespaces and configuration sections retain upstream names; those are not rewritten as part of this branding change and are not a ready Tavchain operator recipe. In particular, scripts/cronos-devnet.yaml is an upstream fixture with unreviewed economic and administrative settings, not the Tavchain network configuration.

The metadata object sets no supply, balances, staking participation, inflation, governance deposits, gas-price floor, faucet amounts or validator permissions. Those belong in the explicit reviewed fresh-network profile. The first-public-testnet staking/reward deferral remains in force. Historical six-decimal Tavchain state must not be imported or reinterpreted as this fresh18-decimal network.

References: upstream Makefile/root.go/config prefix files at616274a74d4f4747e67fad7f895c000e90a3ec6a; Celo https://docs.celo.org/build/tools/wallets/metamask/setup and https://docs.celo.org/learn/network/overview ; Base https://docs.base.org/get-started/connect-to-base .

> Tavchain modifications (2026): executable identity, address prefixes and network/asset metadata. These modifications are licensed under the Apache License, Version 2.0. Existing upstream notices and third-party licenses are retained. See TAVCHAIN-MODIFICATIONS.md and licenses/Apache-2.0.txt.
