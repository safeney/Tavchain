import hardhatToolboxViem from "@nomicfoundation/hardhat-toolbox-viem";
import { configVariable, defineConfig } from "hardhat/config";

const compiler = {
  version: "0.8.21",
  settings: { optimizer: { enabled: true, runs: 200 }, evmVersion: "shanghai" },
};

export default defineConfig({
  plugins: [hardhatToolboxViem],
  solidity: { profiles: { default: compiler, production: compiler } },
  networks: {
    hardhatMainnet: { type: "edr-simulated", chainType: "l1", hardfork: "shanghai" },
    tavchain: {
      type: "http",
      chainType: "l1",
      url: "https://api.testnet.tavchain.safeney.com/",
      chainId: 771002,
      accounts: [configVariable("TAVCHAIN_PRIVATE_KEY")],
    },
  },
  chainDescriptors: {
    771002: {
      name: "Tavchain Testnet",
      blockExplorers: {
        blockscout: {
          name: "Tavchain Explorer",
          url: "https://explorer.tavchain.safeney.com",
          apiUrl: "https://explorer.tavchain.safeney.com/api",
        },
      },
    },
  },
  verify: {
    etherscan: { enabled: false },
    sourcify: { enabled: false },
    blockscout: { enabled: true },
  },
});
