#requires -version 5.1
param(
    [ValidateSet("init", "start", "help")][string]$Action = "help",
    [string]$NodeHome = (Join-Path $env:USERPROFILE ".tavchain-testnet-771002")
)
$ErrorActionPreference = "Stop"
if ($Action -eq "help") {
    Write-Output "Usage: .\tavchain-node.ps1 init|start [-NodeHome <absolute-path>]"
    exit 0
}
if ($env:OS -ne "Windows_NT") { throw "This package requires Windows." }
$Architecture = if ($env:PROCESSOR_ARCHITEW6432) { $env:PROCESSOR_ARCHITEW6432 } else { $env:PROCESSOR_ARCHITECTURE }
if ($Architecture -ne "AMD64") { throw "This package requires Windows x86-64." }
if (-not [System.IO.Path]::IsPathRooted($NodeHome)) { throw "Node home must be an absolute path." }
$NodeHome = [System.IO.Path]::GetFullPath($NodeHome)
$Bundle = Get-Content -LiteralPath (Join-Path $PSScriptRoot "PACKAGE-FILES.json") -Raw | ConvertFrom-Json
foreach ($File in $Bundle.PSObject.Properties) {
    $Actual = (Get-FileHash -LiteralPath (Join-Path $PSScriptRoot $File.Name) -Algorithm SHA256).Hash.ToLowerInvariant()
    if ($Actual -cne $File.Value) { throw "Package integrity check failed. Stop and verify the download." }
}
$Executable = Join-Path $PSScriptRoot "bin\tavchaind.exe"
$Marker = Join-Path $NodeHome ".tavchain-native-bundle"
if ($Action -eq "init") {
    if (Test-Path -LiteralPath $NodeHome) { throw "Node home already exists. Keep it; do not initialize again." }
    New-Item -ItemType Directory -Path $NodeHome | Out-Null
    $User = [System.Security.Principal.WindowsIdentity]::GetCurrent().User
    $System = New-Object System.Security.Principal.SecurityIdentifier("S-1-5-18")
    $Acl = New-Object System.Security.AccessControl.DirectorySecurity
    $Acl.SetAccessRuleProtection($true, $false)
    foreach ($Identity in @($User, $System)) {
        $Rule = New-Object System.Security.AccessControl.FileSystemAccessRule($Identity, "FullControl", "ContainerInherit,ObjectInherit", "None", "Allow")
        $Acl.AddAccessRule($Rule)
    }
    Set-Acl -LiteralPath $NodeHome -AclObject $Acl
    & $Executable init my-tavchain-fullnode --chain-id tavchaintestnet_771002-1 --default-denom atav --home $NodeHome
    if ($LASTEXITCODE -ne 0) { throw "Initialization failed; keep the partial home for inspection." }
    foreach ($Name in @("genesis.json", "config.toml", "app.toml")) {
        Copy-Item -LiteralPath (Join-Path $PSScriptRoot ("network\" + $Name)) -Destination (Join-Path $NodeHome "config")
    }
    Set-Content -LiteralPath $Marker -Value "tavchaintestnet_771002-1" -Encoding ascii
    Write-Output "Initialized $NodeHome. Start with: .\tavchain-node.ps1 start"
} else {
    if (-not (Test-Path -LiteralPath $Marker -PathType Leaf)) { throw "Home is not initialized by this bundle. Do not overwrite existing state." }
    if ((Get-Content -LiteralPath $Marker -Raw).Trim() -cne "tavchaintestnet_771002-1") { throw "Wrong network marker." }
    & $Executable start --home $NodeHome --genesis_hash a101ab9ccf1478757af8a69d832548ea1167e552fe6d6ef6621a77447a54e924
    exit $LASTEXITCODE
}
