> Use Tavchain Testnet, chain ID 771002. Check the RPC chain ID before deploying. Predecessor-network deployments do not carry forward.

# Tavchain Hardhat starter

Build, test, deploy and verify the fictional Gold (GLD) ERC-20 example with standard Hardhat 3, viem and Ignition. Gold is a demonstration token, not gold-backed or an official Tavchain asset. TAV pays gas fees; GLD is the example contract token. Both use 18 decimals.

## Requirements and local workflow

Use a maintained, even-numbered Node.js release supported by Hardhat, at least 22.13.0. The accepted run used Node 24.22.1 on Linux x64. Windows/macOS and a clean external-machine installation are not yet tested. Internet is needed for dependencies and compiler downloads.

```sh
npm ci --ignore-scripts
npm run typecheck
npm run build
npm test
npx hardhat ignition deploy ignition/modules/GLDToken.ts --network hardhatMainnet
```

The three tests check fixed supply/metadata, a ten-token transfer with event/balances, and rejected overdraw preserving state. Local Hardhat fixture accounts are publicly known. Never fund them with valuable assets. The local deployment ends with its in-process network.

Compiler profiles default and production use Solidity 0.8.21, optimizer enabled/200 runs and Shanghai. Initial supply is 1,000 GLD (1000 × 10^18 raw units). Exact dependency versions/integrities are in package-lock.json.

## Read Tavchain without signing

```sh
npx hardhat run scripts/read-network.ts
```

This reads the public chain ID and block height. It requires no existing contract, reads no token balance and submits no transaction. Chain ID must be 771002.

## Store a dedicated test key

Use a fresh account holding only valueless Test TAV. Obtain Test TAV from https://faucet.tavchain.safeney.com/. Do not use an operational or valuable mainnet account or export a recovery phrase.

```sh
npx hardhat keystore set TAVCHAIN_PRIVATE_KEY
```

Hardhat asks privately for a keystore password and the dedicated account's private key. Keep both private; never put either in source files, command arguments, chat or version control. Use the encrypted production keystore, not --dev. A compromised host/dependency can expose the key while unlocked. Do not use keystore get, which prints the secret.

## Deploy publicly

Run this once and check Hardhat's network and deployer before confirming. It submits a real testnet transaction with zero native value and spends Test TAV gas.

```sh
npx hardhat --config hardhat.public.config.ts ignition deploy ignition/modules/GLDToken.ts --network tavchain
```

The public configuration is byte-for-byte the tested trial configuration under a clearer filename. It uses a maximum fee of 2 gwei/gas, priority fee 0.125 gwei, five confirmations and no automatic fee increases. These are example client settings, not Tavchain protocol limits. Check current fees before deploying; these settings may become unsuitable as conditions change. They are not a total-fee guarantee. Retain Ignition's deployment journal and your contract address/hash. If interrupted or unclear, check the journal, wallet nonce and receipt before any rerun; do not use --reset to create a second deployment.

## Verify without a signing key

Replace CONTRACT_ADDRESS with your successful deployment's address:

```sh
npx hardhat --config hardhat.verify.config.ts verify blockscout --network tavchain CONTRACT_ADDRESS 1000000000000000000000
```

This configuration uses Hardhat's standard remote account mode solely for a keyless verifier connection; it does not unlock an account on Tavchain's RPC. It imports the same compiler/plugins/explorer descriptors. Verification requires no key/password, signature or TAV payment. It publishes source/imports/compiler settings to the hosted explorer verifier and polls for a result.

Use the artifact that actually deployed the contract. Local npm imports differ from Remix's versioned imports; do not mix the builds or rename compiler input entries. A missing TAVCHAIN_PRIVATE_KEY error during verification indicates the signing configuration was selected; use hardhat.verify.config.ts rather than exposing a key to CI. The Blockscout provider needs no Etherscan API key. Check the contract page for exact match before treating verification as complete.

## Accepted public example

On Tavchain Testnet, chain ID 771002, Hardhat Ignition deployed 1,000 GLD to the dedicated deployer. Creation/runtime, mint event, metadata, supply and balance matched. Blockscout verification matched the exact source and compiler settings, including five OpenZeppelin imports.

- Contract: https://explorer.tavchain.safeney.com/address/0x9FEE6A0eAf071Dc6fFa1B6193cE1ab52E085F525?tab=contract
- Deployment: https://explorer.tavchain.safeney.com/tx/0xa62f6eedb3453475d819dbf865fce933cdcdae4e13604d37f135326f91a3b12c
- Deployment block: 10792
- Gas used: 545,641
- Fee: 0.000613846125 Test TAV, an observed fee, not a future quote

A [10-GLD transfer](https://explorer.tavchain.safeney.com/tx/0xa78e1dfc1c66accb0e24bf3d9a1027af564d04382d80a49f7979dcb4f732e7f4) succeeded at block 10833. At that block, the deployer held 990 GLD and the recipient held 10 GLD; total supply remained 1,000 GLD. Deployment and transfer fees totaled 0.000671911875 Test TAV. Later activity may change balances. This starter includes a deployment module; use the [token guide](https://docs.tavchain.safeney.com/tavchain/erc20-token#transfer-10-gld) for your own transfer. Source verification is not a security audit or official-token designation. The explorer's separate license metadata is none; the source retains its MIT SPDX notice and this kit includes its MIT license and third-party notices.

## Links and license

- Guide: https://docs.tavchain.safeney.com/tavchain/hardhat
- RPC: https://api.testnet.tavchain.safeney.com/
- Chain ID: 771002
- Browser tutorial: https://docs.tavchain.safeney.com/tavchain/erc20-token

This source kit uses MIT terms in LICENSE, preserving third-party rights/notices in THIRD-PARTY-NOTICES.md. Dependencies are fetched by npm, not bundled. No Tavchain node binary, node source, credential, keystore, dependency directory, build artifact or deployment journal is shipped. The released starter ZIP is listed in the network release's signed NETWORK-RELEASE.json; follow its [verification instructions](https://github.com/safeney/Tavchain/releases/download/network-771002-1/VERIFY.md) to authenticate the manifest and archive. A checksum alone detects changed bytes. The Git source directory is editable source, separate from that unchanged signed ZIP; use the current guide for network and example references.
