import { defineConfig } from "hardhat/config";
import base from "./hardhat.config.js";

export default defineConfig({
  ...base,
  networks: {
    ...base.networks,
    tavchain: {
      ...base.networks!.tavchain,
      ignition: {
        maxFeePerGasLimit: 2_000_000_000n,
        maxFeePerGas: 2_000_000_000n,
        maxPriorityFeePerGas: 125_000_000n,
        disableFeeBumping: true,
      },
    },
  },
  ignition: {
    ...base.ignition,
    disableFeeBumping: true,
    maxFeeBumps: 0,
    requiredConfirmations: 5,
  },
});
