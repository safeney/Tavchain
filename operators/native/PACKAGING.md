# Native bundle packaging

Launchers and this packaging guide are released under Apache-2.0. Existing clients, dependencies and runtime libraries retain their original notices and terms.

Use the native1 client archives authenticated by NATIVE-RELEASE.json and network files authenticated by NETWORK-RELEASE.json. Keep original client/runtime bytes unchanged under bin/, and the three current network files under network/. Include original manifests/signatures under provenance/ and required notice archives. Windows keeps all four DLLs beside the executable.

Copy the matching launcher and README.md into the bundle root. Linux ARCH contains amd64 or arm64. SHA256SUMS (Linux) or PACKAGE-FILES.json (Windows) lists every other regular file and SHA256. Create one tar.gz per Linux target and a ZIP for Windows. The separately signed BUNDLE-RELEASE.json authenticates final archives; internal checksums are not publisher authentication.

Use the authenticated native1 source archive from the linked native1 release for client reproduction. The public node/ snapshot predates that exact native packaging.
