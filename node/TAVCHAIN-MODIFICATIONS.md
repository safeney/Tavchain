# Tavchain modifications and source permissions

Sir approved EVMSOURCEPOLICY1 on29October2026. Tavchain modifications to the eight paths listed below are licensed under the Apache License, Version2.0. Existing upstream copyright notices, licenses and attribution are retained. Dependencies retain their own licenses. The full Apache2.0 text is in licenses/Apache-2.0.txt.

Upstream Cronos commit616274a74d4f4747e67fad7f895c000e90a3ec6a; original identity/network patch SHA256c2a86d91e622a19d944686549e3ab6d007977ff69ae8cd03b490fb17ce745e3f. Release-only prominent modification notices were appended to the changed source files; the JSON bank metadata's existing description carries its notice. These release notices do not alter the installed binary, public genesis, consensus rules or allocations.

The original source networks/README.md is a historical pre-deployment candidate note, not a statement of current public-network status. Current operator instructions and the actual sealed public genesis are in the binary/network package. Do not construct a new genesis from a historical source README to join the retained testnet.

- Makefile
- app/app.go
- cmd/cronosd/cmd/root.go
- cmd/cronosd/config/prefix_mainnet.go
- cmd/cronosd/config/prefix_testnet.go
- cmd/cronosd/main.go
- networks/README.md
- networks/native-asset-metadata.json
