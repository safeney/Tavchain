import { buildModule } from "@nomicfoundation/hardhat-ignition/modules";

export default buildModule("GLDTokenModule", (m) => {
  const initialSupply = m.getParameter("initialSupply", 1000n * 10n ** 18n);
  const token = m.contract("GLDToken", [initialSupply]);
  return { token };
});
