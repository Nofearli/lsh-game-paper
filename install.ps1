# Install the lsh-game-paper skill into a skills directory.
#
#   powershell -ExecutionPolicy Bypass -File .\install.ps1                # -> ~\.agents\skills\lsh-game-paper
#   powershell -ExecutionPolicy Bypass -File .\install.ps1 C:\skills      # custom root
#   powershell -ExecutionPolicy Bypass -File .\install.ps1 -Force         # overwrite without asking
param(
    [string]$Root = (Join-Path $env:USERPROFILE ".agents\skills"),
    [switch]$Force
)

$ErrorActionPreference = "Stop"
$Src = $PSScriptRoot
$Dest = Join-Path $Root "lsh-game-paper"

New-Item -ItemType Directory -Force -Path $Root | Out-Null

if (Test-Path $Dest) {
    if (-not $Force) {
        $ans = Read-Host "Destination exists: $Dest`nOverwrite? [y/N]"
        if ($ans -notmatch '^[yY]') { Write-Output "Aborted."; exit 1 }
    }
    Remove-Item -Recurse -Force $Dest
}

 robocopy $Src $Dest /E /XD .git __pycache__ | Out-Null
if ($LASTEXITCODE -ge 8) { throw "robocopy failed with exit code $LASTEXITCODE" }

Write-Output "Installed to: $Dest"
Write-Output "Verify with:  python `"$Dest\scripts\citation_checker.py`" --check-library"
