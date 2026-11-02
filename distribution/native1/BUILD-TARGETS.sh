#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/tavchain-source"
nix --version
for path in default.nix flake.nix nix/bundle-win-exe.nix nix/cronos-matrix.nix; do
    nix-instantiate --parse "$path" >/dev/null
done
nix flake metadata --no-update-lock-file --no-write-lock-file path:$PWD
for target in linux-amd64 linux-arm64 windows-amd64; do
    case "$target" in
        linux-amd64) package="legacyPackages.x86_64-linux.pkgsStatic.cronos-matrix.cronosd-testnet" ;;
        linux-arm64) package="legacyPackages.x86_64-linux.pkgsCross.aarch64-multiplatform.pkgsStatic.cronos-matrix.cronosd-testnet" ;;
        windows-amd64) package="legacyPackages.x86_64-linux.pkgsCross.mingwW64.cronos-matrix.cronosd-testnet" ;;
    esac
    test "$(nix eval --raw --no-update-lock-file --no-write-lock-file "path:$PWD#$package.pname")" = "tavchaind"
    test "$(nix eval --raw --no-update-lock-file --no-write-lock-file "path:$PWD#$package.version")" = "1.8.1-tavchain.eval1-native1"
    test "$(nix eval --raw --no-update-lock-file --no-write-lock-file "path:$PWD#$package.go.version")" = "1.25.11"
    test "$(nix eval --raw --no-update-lock-file --no-write-lock-file "path:$PWD#$package.CGO_ENABLED")" = "1"
    test "$(nix eval --raw --no-update-lock-file --no-write-lock-file "path:$PWD#$package.tags" --apply 'tags: builtins.concatStringsSep "," tags')" = "netgo,testnet,pebbledb,objstore,nativebyteorder"
    nix build --no-update-lock-file --no-write-lock-file --no-allow-dirty -L --out-link "../$target-result" "path:$PWD#${package}-tarball"
done
