# Tavchain native full-node bundle

Download and authentication:
https://github.com/safeney/Tavchain/releases/tag/native-bundle-771002-1

Authenticate the release archive before executing its contents. Follow the release's VERIFY.md.
Included checksum checks detect changed package files; they do not independently authenticate this launcher or publisher.

The bundle combines the native1 client and 771002 network profile.
Linux: extract the matching archive, then run `./tavchain-node init` once and `./tavchain-node start`.
Windows x86-64: extract the ZIP with all included DLLs, then run `.\tavchain-node.ps1 init` once and `.\tavchain-node.ps1 start` from PowerShell.

If Windows blocks a downloaded script, stop. Authenticate the archive and review the script before following VERIFY.md's per-file unblocking guidance. Do not disable or bypass execution policy or organization restrictions. This SSH-signed archive is not an Authenticode signature for the PowerShell script.

Default data home: your user directory's `.tavchain-testnet-771002`. Supply the same optional absolute home on each invocation if you change it.
Initialization refuses an existing home. Partial initialization is retained for inspection.
Startup reuses state and supplies the pinned genesis hash; it does not replace retained configuration.
Keep RPC private; local native status is http://127.0.0.1:29657/status.
Wait for advancing heights and catching_up=false. Zero voting power is normal.
No wallet, stake, registration, administrator privileges or service installation is required.

Native initialization, synchronization, state comparison and graceful same-identity restart passed on GitHub-hosted Ubuntu 24.04 x64/ARM64 and Windows Server 2022 x64.
Linux termination used SIGTERM and Windows used the console Ctrl+Break event.
Browser-download file blocking, all terminal interrupt modes, long-duration reliability and validator signing are not established by those trials.
No macOS or Windows ARM64 support is asserted.
Interrupt the process in its terminal and wait for shutdown; avoid Task Manager for routine Windows termination.
Node guide: https://docs.tavchain.safeney.com/tavchain/operate/node-native
Support: support@safeney.com
