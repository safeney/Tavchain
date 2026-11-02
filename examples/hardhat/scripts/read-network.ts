import { createPublicClient, defineChain, http } from "viem";

const tavchain = defineChain({
  id: 771002,
  name: "Tavchain Testnet",
  nativeCurrency: { name: "Test Tavcoin", symbol: "TAV", decimals: 18 },
  rpcUrls: { default: { http: ["https://api.testnet.tavchain.safeney.com/"] } },
  testnet: true,
});
const client = createPublicClient({ chain: tavchain, transport: http(undefined, { retryCount: 0 }) });
const chainId = await client.getChainId();
if (chainId !== tavchain.id) throw new Error(`Unexpected chain ID: ${chainId}`);
const block = await client.getBlockNumber();
console.log({ chainId, block: block.toString() });
