import assert from "node:assert/strict";
import { describe, it } from "node:test";
import { network } from "hardhat";
import { getAddress, parseUnits } from "viem";

describe("GLDToken", async function () {
  const { viem } = await network.create();
  const [owner, recipient] = await viem.getWalletClients();
  const supply = parseUnits("1000", 18);

  it("mints the fixed supply to the deployer with standard metadata", async function () {
    const token = await viem.deployContract("GLDToken", [supply]);
    assert.equal(await token.read.name(), "Gold");
    assert.equal(await token.read.symbol(), "GLD");
    assert.equal(await token.read.decimals(), 18);
    assert.equal(await token.read.totalSupply(), supply);
    assert.equal(await token.read.balanceOf([owner.account.address]), supply);
  });

  it("transfers ten GLD with a matching Transfer event and balances", async function () {
    const token = await viem.deployContract("GLDToken", [supply]);
    const amount = parseUnits("10", 18);
    await viem.assertions.emitWithArgs(
      token.write.transfer([recipient.account.address, amount]),
      token,
      "Transfer",
      [getAddress(owner.account.address), getAddress(recipient.account.address), amount],
    );
    assert.equal(await token.read.balanceOf([owner.account.address]), supply - amount);
    assert.equal(await token.read.balanceOf([recipient.account.address]), amount);
    assert.equal(await token.read.totalSupply(), supply);
  });

  it("rejects an overdraw without changing balances or supply", async function () {
    const token = await viem.deployContract("GLDToken", [supply]);
    await viem.assertions.revertWithCustomErrorWithArgs(
      token.write.transfer([recipient.account.address, supply + 1n]),
      token,
      "ERC20InsufficientBalance",
      [getAddress(owner.account.address), supply, supply + 1n],
    );
    assert.equal(await token.read.balanceOf([owner.account.address]), supply);
    assert.equal(await token.read.balanceOf([recipient.account.address]), 0n);
    assert.equal(await token.read.totalSupply(), supply);
  });
});
