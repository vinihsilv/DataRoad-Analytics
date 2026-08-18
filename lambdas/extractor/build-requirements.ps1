# Regenera requirements.txt a partir do grupo "extractor" do pyproject.toml na raiz do repo.
$ErrorActionPreference = "Stop"

$repoRoot = Resolve-Path (Join-Path $PSScriptRoot "..\..")
$outputPath = Join-Path $PSScriptRoot "requirements.txt"

Push-Location $repoRoot
try {
    poetry export --only main,extractor --without-hashes -f requirements.txt --output $outputPath
}
finally {
    Pop-Location
}

Write-Host "requirements.txt atualizado em $outputPath"
