package main

import (
	"os"

	"github.com/crypto-org-chain/cronos/app"
	"github.com/crypto-org-chain/cronos/cmd/cronosd/cmd"

	svrcmd "github.com/cosmos/cosmos-sdk/server/cmd"
	sdk "github.com/cosmos/cosmos-sdk/types"
)

func init() {
	// Pin sdk.GetConfig()'s scope key so getConfigKey() skips the
	// os.Executable() + os.Hostname() syscalls on every call (hot during
	// bech32 address coding).
	//
	// NOTE: process-global and runs before flag parsing, so operators must
	// export COSMOS_SDK_CONFIG_SCOPE before launch to override. The LookupEnv
	// guard only avoids overwriting an existing value.
	if _, ok := os.LookupEnv(sdk.EnvConfigScope); !ok {
		_ = os.Setenv(sdk.EnvConfigScope, "tavchain")
	}
}

func main() {
	rootCmd := cmd.NewRootCmd()
	if err := svrcmd.Execute(rootCmd, cmd.EnvPrefix, app.DefaultNodeHome); err != nil {
		os.Exit(1)
	}
}

// Tavchain modifications (2026): executable identity, address prefixes and network/asset metadata. These modifications are licensed under the Apache License, Version 2.0. Existing upstream notices and third-party licenses are retained. See TAVCHAIN-MODIFICATIONS.md and licenses/Apache-2.0.txt.
