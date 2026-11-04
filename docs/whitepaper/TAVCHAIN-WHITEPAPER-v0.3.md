# Tavchain

## A General-Purpose EVM Blockchain for Applications and Payments

**Whitepaper v0.3 | Testnet edition | 4 November 2026**

Tavchain / Safeney

This whitepaper explains Tavchain's purpose, public-testnet architecture, native coin and development direction. It distinguishes available capabilities from proposed integrations and mainnet economic decisions that remain open.

# Executive summary

Tavchain is a general-purpose, EVM-compatible Layer 1 blockchain for smart contracts and applications. Its purpose is to provide shared infrastructure through which developers can build services that help people, businesses and institutions transact, verify information and collaborate. Its direction is shaped by Africa's needs and open to builders worldwide. [1]

The platform supports applications rather than prescribing one business model or industry. Payments, finance and DeFi are important opportunities alongside digital assets, commerce, games and verifiable records. These applications require more than a blockchain: usable interfaces, reliable data and, where relevant, asset issuers, payment providers and commercial agreements.

Tavchain builds on existing open-source technology. The node derives from Cronos 1.8.1 and combines EVM execution, Cosmos SDK application modules and CometBFT-family consensus. Developers use Solidity, Ethereum-style accounts and familiar tools. Validators operate Tavchain's own consensus; the chain does not settle to Ethereum. [1][2][3]

Tavcoin, abbreviated TAV, is the native coin. In the current network, Test TAV supports transaction fees, native transfers, staking, delegation and governance participation. Test TAV has no monetary value. The testnet's allocations and economic parameters do not establish mainnet supply, distribution or redemption rights. [4][5][6][7]

The public testnet provides wallet access, contract deployment and interaction, source verification, a faucet, an explorer and published full-node software. Its initial four validators remain under shared administration. Broader independent operation, reliable application integrations and evidence-backed economic decisions are development priorities. [3][9]

Tavchain's direction is an application ecosystem with familiar EVM tools and its own network participation, native-coin economics and protocol evolution. The current foundation supports developers building and evaluating applications. Broader financial services depend on application teams, sustainable network operation and external integrations.

# 1. Purpose and intended users

## 1.1 Shared infrastructure for useful applications

Tavchain's mission begins with practical application needs. People and organizations may need to coordinate payments, apply agreed rules to assets, verify that records have not changed or exchange information across organizational boundaries. A blockchain can provide a common execution and verification layer when participants need independently checkable state and cannot rely entirely on one application's database.

An application can, for example, hold a token payment under an escrow rule, issue a transferable membership or anchor a document hash for later verification. Each example still needs an application team, suitable interfaces and clear responsibility for off-chain facts. An escrow contract cannot observe delivery by itself. A document hash can establish a match with submitted bytes, but cannot establish that the document's claims are true.

Tavchain's Africa-informed direction concerns which problems receive attention and how applications are made usable. It does not assume that all African countries have the same infrastructure, payment systems, currencies or rules. Deployments must be designed for their actual users and providers. The same infrastructure can serve applications elsewhere.

## 1.2 A general-purpose platform

Tavchain does not make one application the sole purpose of the chain. Developers can define their own contract logic and user experience within the network's capabilities. The initial developer foundation is EVM compatibility: existing Solidity knowledge, Ethereum account conventions and established development tools reduce the need for an unfamiliar application environment. Compatibility must still be checked for the particular library, compiler settings and contract behavior involved. [1][9]

Three audiences guide the platform:

- Application developers need clear interfaces, working examples, predictable network identity and inspectable execution.
- Users need understandable actions, appropriate fee information and control of their signing keys.
- Node operators and contributors need public software, authenticated releases, explicit trust assumptions and maintainable upgrade procedures.

No node installation is required for a user or application to use the public RPC service. Operating a node is a separate choice for verification, infrastructure or protocol participation.

# 2. Why a separate Layer 1?

## 2.1 A platform with its own evolution

A separate Layer 1 allows Tavchain's protocol and participants to define its own validator participation, native-asset rules, governance and software evolution. These are the design levers that make a sovereign network different from an application deployed as contracts on another chain.

That control comes with responsibility. Tavchain must sustain its own consensus security, operator participation, infrastructure and developer ecosystem. An existing EVM network may already provide stronger liquidity, wider integrations and more independent infrastructure. EVM compatibility makes many tools familiar; it does not transfer another network's validators, liquidity or economic security.

Tavchain's direction is to build an EVM application ecosystem whose network participation, native-coin economics and protocol evolution can develop together. Applications can share a common execution layer while their developers retain responsibility for their products and integrations. The separate chain provides room to shape those network rules; application contracts and external providers supply the services built on top.

The initial focus is a dependable developer foundation, followed by simpler payment and financial-application journeys. Fee sponsorship and connections to suitable asset and payment providers are development directions. They are not evidence of native multi-token gas, fiat liquidity or a live stablecoin service. A separate Layer 1 is justified only as these capabilities and its operator ecosystem become useful in practice.

## 2.2 Goals and how to assess them

The development goals are clear application access, useful contract tooling, verifiable operation and a path toward broader participation. Progress should be assessed through reproducible user journeys, supported-platform checks, independent node and validator operation, transparent fees and useful applications.

A future performance claim should state its software version, validator topology, hardware, workload, measurement interval and failure conditions. This paper makes no transactions-per-second, universal low-cost or guaranteed-availability claim. A fast isolated test cannot establish production capacity.

# 3. Architecture and technology provenance

## 3.1 Protocol layers

Tavchain's node application integrates three main responsibilities. EVM execution processes supported smart-contract calls and Ethereum-style transactions. Cosmos SDK modules provide native application mechanisms including staking, distribution, slashing and governance. CometBFT-family consensus coordinates the active validators' agreement on committed blocks. [1][2]

A conceptual transaction path is:

**Wallet or application -> JSON-RPC node -> transaction validation and propagation -> validator consensus and execution -> committed state and receipt -> application or explorer display.**

The explorer is an indexing and presentation service. It is not the consensus authority. An indexing delay may affect what an explorer shows even while the chain continues producing blocks. Likewise, a reachable website is not proof that the chain is progressing.

## 3.2 Interfaces and identity

Applications use Ethereum JSON-RPC for queries, gas estimation and signed EVM transaction submission. Native tooling uses separate native identifiers and interfaces. Use the correct network and address representation for each operation. [10]

The current public testnet uses EVM chain ID **771002** and native chain ID **tavchaintestnet_771002-1**. These identify the testnet described here. A future mainnet must have its own published identity and release configuration; this paper does not assign one.

A familiar account or contract address does not identify a chain. Software should check network identity before requesting a signature. Published configuration and authenticated releases provide the operational reference.

## 3.3 Validators, full nodes and services

An active validator has consensus voting power and participates in committing blocks. A non-validator full node follows and verifies the chain without contributing consensus votes. Running a full node, receiving test tokens and registering a validator are distinct actions. Registration alone does not guarantee entry into the active set. [5]

RPC, explorer, faucet and status reporting have different trust and availability boundaries. Public RPC users depend on their provider; an independently operated full node provides a separate verification route.

## 3.4 Inherited technology and Tavchain changes

Tavchain does not claim to have invented the EVM, Cosmos SDK or CometBFT consensus. Its published source includes upstream attribution and a record of changes to eight paths covering application configuration, command identity, address prefixes, build and network metadata. These modifications must not be presented as a new consensus design. [11]

The node source is distributed under Apache 2.0, with upstream notices and dependency terms retained. Released packaging and dependencies have their own included notices. Public code supports inspection and contributions; it does not expose or grant control of validator keys, wallets or infrastructure administration.

# 4. Consensus, security and participation

## 4.1 Finality and availability

A block is committed after valid precommits representing more than two-thirds of the current validator voting power. Under the protocol's consensus assumptions, including less than one-third faulty voting power, committed blocks have deterministic finality. The threshold concerns voting power, not a simple count of machines. Quorum loss can stop new blocks. [3]

Tavchain is a Layer 1 with its own validator security model. Its EVM interface does not mean that Ethereum secures or settles its blocks. Additional confirmations do not remove the risks associated with shared validator administration.

## 4.2 Current control model

The initial public-testnet set consists of four validators under shared administration. Several share a hosting failure domain. They must not be represented as four independent organizations or four independent security domains. A shared outage can affect consensus availability; compromise of sufficient voting power can compromise network security. [3]

Broader participation requires separately controlled operators with their own key custody and operational responsibility. More processes on the same controlled hosts do not establish decentralization. The current public release documentation identifies independent operator acceptance as pending. [9]

## 4.3 Staking and delegation

The testnet uses the native staking module with atav as its bond denomination. Validators register consensus public keys and self-delegation using native tools. Delegators bond Test TAV to validators. Active membership is selected by bonded stake within the configured set limit, currently up to ten validators. [5]

The documented testnet unbonding period is 21 days. Downtime and double-signing penalties can affect staked funds. Commission rates are declared by validators within their configured constraints. Users must inspect the current parameters and validator information before acting; these figures are testnet settings rather than immutable mainnet commitments.

## 4.4 Layered security responsibility

Consensus security, contract correctness, wallet safety and service reliability are separate concerns. A successful receipt establishes an execution result recorded in a block; it does not establish the safety or value of an application. Verified source links published code to deployed bytecode under the verifier's matching rules; it is not a security certification.

The current testnet is unaudited. Security work includes implementation review, automated checks, scoped runtime acceptance, public source inspection and private vulnerability reporting. This paper does not assert that these activities eliminate defects or constitute an independent audit.

Wallet recovery phrases and private keys remain with their owners. Public services and support do not need them. Security reports should be sent privately to **support@safeney.com** with enough information for safe investigation and without credentials or personal data.

# 5. Tavcoin and network economics

## 5.1 Native asset roles

Tavcoin, or TAV, is the network's native coin. It has 18 decimal places; one TAV equals 10^18 atav. Native transfers move TAV between accounts. Network fees are paid in TAV. Native staking, delegation and governance use the chain's native modules and voting-power rules. [4][5][7]

Application tokens such as ERC-20s are separate assets defined by contracts. Their names and symbols do not establish issuer identity, backing or value. Their balances do not automatically replace the TAV required for network fees. An application's token policy must be evaluated independently of native network economics.

## 5.2 Current testnet allocation

The testnet genesis allocates **1,000,000 Test TAV**. Four operator accounts receive 2,000 each; the faucet receives 50,000; a validator-grant reserve receives 50,000; and the test reserve receives 892,000. Each initial validator self-bonds 1,000 Test TAV from its operator allocation. The reserve does not automatically refill the faucet. [4]

These allocations support network development. Test TAV has no monetary value, and test balances have no announced redemption, airdrop or mainnet conversion entitlement. This allocation is not a mainnet distribution schedule.

## 5.3 Current fee distribution

The testnet distributes transaction fees through the native distribution module. Its configured inflation rate is zero. The community pool receives 2% of distributed fees; validator commission and delegator shares are accounted for by the module. Empty blocks do not create an inflation subsidy. Accrued accounting, withdrawable rewards and withdrawn wallet balances are distinct. [6]

No fixed return is promised. Activity, stake, commission and applicable rules affect distribution. On a future valuable-asset network, security sustainability would require a deliberate assessment of operator costs, fee demand and any approved issuance or funding policy. Testnet configuration alone does not establish an economically sustainable mainnet.

## 5.4 Mainnet economic decisions

This edition does not set mainnet total supply, issuance, allocations, vesting, treasury controls, validator subsidies, grant policy or sale terms. Those decisions require a separate economic design and explicit approval. The eventual published design should explain who can change parameters, how changes take effect and how participants can evaluate supply and distribution.

The role of TAV is protocol utility. This paper provides no price forecast, exchange-listing commitment or assurance of financial return.

# 6. Application and payment experience

## 6.1 Developer access

Developers can build and interact with Solidity contracts using the documented Remix and Hardhat workflows. The published tutorials include simple contract and ERC-20 examples with deployment and verification guidance. The reference compiler settings use Solidity 0.8.21 with a Shanghai EVM target; other combinations require their own compatibility checks. [9]

Wallet users connect a supported custom EVM network, obtain Test TAV and submit reviewed actions. Node operators can use published native bundles or the separately documented Docker route. Supported full-node downloads include Linux x86-64, Linux ARM64 and Windows x86-64. These non-validator acceptance results do not establish validator-signing support for every platform. [9]

The detailed setup, API limits and release commands belong in living documentation. Keeping those instructions separate allows the whitepaper to explain the design without becoming an installation manual.

## 6.2 Payments and financial applications

Contracts can express token transfers, escrow conditions, asset issuance and financial application rules. The network provides shared execution; applications provide their products, risk controls and users' interfaces. Neither EVM compatibility nor a token contract creates fiat convertibility, issuer-backed stablecoins or reliable price feeds.

On-ramps and off-ramps connect blockchain assets to external payment systems. Their availability depends on providers, supported networks and assets, liquidity and the arrangements required for each market. They cannot be created merely by declaring support in a whitepaper. Tavchain's current public release does not provide an official bridge or IBC asset-transfer route. [8][9]

Stablecoin and payment-provider connectivity are development opportunities. No confirmed partner, supported fiat corridor or available real-money product.

## 6.3 Fee sponsorship direction

A user experience can hide the need to hold native gas without changing the underlying fee asset. A sponsor-funded smart-account flow pays network fees in TAV on the user's behalf. A token-reimbursement flow can charge a supported application token while the sponsor or bundler still pays TAV underneath.

Fee sponsorship and supported-token reimbursement are development directions. A user-facing service would need to demonstrate bounded permission, transfer, charge/refund accounting and allowance removal on its actual deployment. This paper does not claim public availability, real-token pricing, rebalancing liquidity, all-wallet compatibility or unrestricted sponsorship.

A public service would need funded fee capacity, supported-action rules, authenticated ownership, durable request accounting and a clear recovery path. It should show the action, fee limit and spending permission before signing. Future token reimbursement must explain who bears exchange-rate and liquidity risk. No such service is announced as publicly available by this paper.

# 7. Governance and software evolution

The current testnet uses native governance based on bonded voting power. It is not one-wallet-one-vote. Ordinary proposals currently require a minimum deposit of 100 Test TAV and have a 24-hour voting period. Documented quorum is 0.334, approval threshold 0.5 and veto threshold 0.334 under the native tally rules. Expedited proposals require 500 Test TAV and have a six-hour voting period. [7]

These parameters do not fully describe every proposal outcome. Native rules distinguish voting options and deposit outcomes. Passing a vote does not guarantee that a requested action executes successfully. Software upgrades also require compatible releases and coordinated operator procedures.

Source maintenance and protocol governance are distinct. A repository contribution or merge does not itself change the running network. Conversely, an onchain decision does not make operators independently controlled or automatically perform every required infrastructure action.

A mainnet governance design must clearly describe authority, supported changes, operational adoption and the limits of emergency intervention. This paper does not create new governance powers or promise a particular mainnet constitution.

# 8. Evidence and current boundaries

## 8.1 Public capabilities

As documented on 4 November 2026, Tavchain Testnet provides native transfers, Solidity deployment and interaction, example-token development, contract-source verification, HTTP JSON-RPC, an explorer, a faucet and public full-node software. Native staking, delegation, fee distribution and governance are enabled. [1][5][6][7][9]

Published node checks cover scoped synchronization, state comparison and graceful restart on documented environments. These are evidence of the tested behaviors, not an unlimited-capacity or fault-tolerance guarantee. The descriptions here follow the published release documentation; they are not a new code or onchain audit.

## 8.2 Limits that matter to users

The initial validators are centrally administered. Independent operator acceptance remains pending in the current release documentation. No official bridge, IBC asset-transfer route or mainnet balance conversion is available. Public WebSocket RPC and debug tracing are not offered. Hosted services are best effort and have no uptime SLA. [9]

These boundaries should be updated when accepted evidence and the public deployment change. Private development results must not silently become claims about the live network. The paper's version and references identify its scope; live service status belongs on the status page.

# 9. Development direction and milestones

Tavchain's direction is to improve a reusable platform for useful applications, rather than claim that the blockchain itself supplies every financial or institutional service. The following milestones organize that direction without assigning unapproved launch dates.

**Builder access:** maintain working wallet, contract, verification and node journeys; simplify entry points and publish compatible releases with clear support boundaries.

**Broader participation:** complete acceptance with separately controlled operators and demonstrate that registration, active voting power, key custody and ongoing operation are understood and verifiable.

**Application usability:** develop a public-testnet sponsorship integration with clear permission and fee review. Verify accounting, interrupted requests and allowance cleanup before expanding access.

**Useful integrations:** evaluate provider and application needs with evidence from actual users. Announce corridors, supported assets or partnerships only after concrete arrangements and acceptance exist.

**Mainnet design:** resolve supply and incentives, validator distribution, governance authority, security readiness, operational recovery and asset/provider dependencies before announcing a launch configuration.

Mainnet readiness is a combined technical, operational and economic decision. A whitepaper, repository publication or successful testnet transaction does not by itself settle that decision.

# 10. Open development and review

Tavchain publishes node source and network configuration through **github.com/safeney/Tavchain**. Developers can inspect the implementation and submit contributions under the repository's contribution process. Public software licensing allows reuse under its terms; it does not transfer control of the Tavchain network or ownership of project accounts. [11][12]

The whitepaper should remain versioned alongside its supporting documentation. Significant revisions should identify which protocol release, network state or policy decision changed. Public feedback can improve the paper; sensitive vulnerability reports belong in the private reporting channel.

This edition describes the public testnet and the platform's development direction. Subsequent editions should identify changes to implemented behavior, evidence and approved policy. Mainnet economic decisions remain open.

# References

Current Tavchain sources were retrieved on 4 November 2026. All numbered references are public. Network parameters describe the documented testnet at that date and should be checked against the current release before operational use.

[1] About Tavchain. https://docs.tavchain.safeney.com/tavchain/about

[2] Network architecture. https://docs.tavchain.safeney.com/tavchain/learn/architecture

[3] Consensus, finality and security. https://docs.tavchain.safeney.com/tavchain/learn/security

[4] Tavcoin. https://docs.tavchain.safeney.com/tavchain/learn/tavcoin

[5] Staking and delegation. https://docs.tavchain.safeney.com/tavchain/learn/staking

[6] Network rewards. https://docs.tavchain.safeney.com/tavchain/learn/rewards

[7] Governance and upgrades. https://docs.tavchain.safeney.com/tavchain/learn/governance

[8] Development and roadmap. https://docs.tavchain.safeney.com/tavchain/learn/history

[9] Release status. https://docs.tavchain.safeney.com/tavchain/status

[10] Network information. https://docs.tavchain.safeney.com/tavchain/network

[11] Tavchain modifications and source permissions. https://github.com/safeney/Tavchain/blob/main/node/TAVCHAIN-MODIFICATIONS.md

[12] Tavchain public source repository. https://github.com/safeney/Tavchain

Foundational and comparative reading: Bitcoin's original paper, https://bitcoin.org/bitcoin.pdf ; Ethereum's original whitepaper, https://ethereum.org/whitepaper/ ; the Cosmos original paper, https://github.com/cosmos/cosmos/blob/master/WHITEPAPER.md ; Celo research catalogue, https://celo.org/whitepapers ; Base protocol overview, https://docs.base.org/specifications/base-protocol/overview . These explain related designs and publication approaches, not proof of Tavchain-specific behavior.

# Version history

v0.3 - 4 November 2026. Testnet edition covering purpose, architecture, participation, native-coin economics and development direction. Mainnet economic policy and launch arrangements remain open.
