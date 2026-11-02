import { defineConfig } from "hardhat/config";
import base from "./hardhat.config.js";

export default defineConfig({
  ...base,
  networks: {
    tavchain: {
      type: "http",
      chainType: "l1",
      chainId: 771002,
      url: "https://api.testnet.tavchain.safeney.com/",
      accounts: "remote",
    },
  },
});
