# Word Counter für Kapitel
# Liest Zielwerte aus PROJECT.md
# Verwendung: .\count-words.ps1 "Pfad\zur\Datei.md"

param(
    [Parameter(Mandatory = $true)]
    [string]$FilePath
)

# Finde PROJECT.md (im aktuellen Verzeichnis oder parent)
$projectPath = $null
$searchPath = Get-Location
for ($i = 0; $i -lt 5; $i++) {
    $testPath = Join-Path $searchPath "PROJECT.md"
    if (Test-Path $testPath) {
        $projectPath = $testPath
        break
    }
    $searchPath = Split-Path $searchPath -Parent
}

# Standard-Werte falls PROJECT.md nicht gefunden
$minWords = 1500
$maxWords = 1800

# Zielwerte aus PROJECT.md lesen
if ($projectPath) {
    $projectContent = Get-Content $projectPath -Raw -Encoding UTF8
    
    # Suche nach "Words per Chapter" Zeile: | **Words per Chapter** | 1,500 - 1,800 |
    if ($projectContent -match '\*\*Words per Chapter\*\*.*?\|\s*([\d,]+)\s*-\s*([\d,]+)') {
        $minWords = [int]($Matches[1] -replace ',', '')
        $maxWords = [int]($Matches[2] -replace ',', '')
        Write-Host "[Config] Ziel aus PROJECT.md: $minWords - $maxWords Woerter" -ForegroundColor DarkGray
    }
}

if (-not (Test-Path $FilePath)) {
    Write-Error "Datei nicht gefunden: $FilePath"
    exit 1
}

# Datei lesen
$content = Get-Content $FilePath -Raw -Encoding UTF8

# YAML-Frontmatter entfernen
if ($content.TrimStart() -match '^---\s*\r?\n[\s\S]*?\r?\n---') {
    $content = $content -replace '^\s*---\s*\r?\n[\s\S]*?\r?\n---\s*', ''
}

# Zeilen filtern
$lines = $content -split '\r?\n'
$filteredLines = @()
$inMetaSection = $false

foreach ($line in $lines) {
    # End-Marker (wie "End of Chapter X") überspringen
    if ($line -match '^\s*\*End of Chapter' -or $line -match '^\s*---\s*$') {
        continue
    }
    
    # Session Summary und danach überspringen
    if ($line -match '\[ARMI - SESSION SUMMARY\]') {
        $inMetaSection = $true
        continue
    }
    
    if ($inMetaSection) {
        continue
    }
    
    # Word Count / Next Chapter Zeilen überspringen
    if ($line -match '^\s*\*\*Word Count\*\*:' -or $line -match '^\s*\*\*Next Chapter\*\*:') {
        continue
    }
    
    $filteredLines += $line
}

$content = $filteredLines -join ' '

# Markdown-Formatierung bereinigen
$content = $content -replace '\*\*', ''              # Bold
$content = $content -replace '\*', ''                # Italic
$content = $content -replace '`[^`]+`', ''           # Inline code
$content = $content -replace '\[([^\]]+)\]\([^\)]+\)', '$1'  # Links
$content = $content -replace '#+\s*', ''             # Headers
$content = $content -replace '\s+', ' '              # Normalize whitespace

# Wörter zählen
$words = $content.Trim() -split '\s+' | Where-Object { $_.Length -gt 0 }
$wordCount = $words.Count

# Ausgabe
Write-Host ""
Write-Host "=== WORTANZAHL ===" -ForegroundColor Cyan
Write-Host "Datei: $(Split-Path $FilePath -Leaf)"
Write-Host ""
Write-Host "Woerter:   $wordCount" -ForegroundColor Green
Write-Host "Ziel:      $minWords - $maxWords"
Write-Host ""

# Zielbereich-Check
if ($wordCount -lt $minWords) {
    $diff = $minWords - $wordCount
    $percent = [math]::Round(($wordCount / $minWords) * 100)
    Write-Host "[!] Unter Ziel" -ForegroundColor Yellow
    Write-Host "    Noch $diff Woerter bis Minimum ($percent%)" -ForegroundColor Yellow
}
elseif ($wordCount -gt $maxWords) {
    $diff = $wordCount - $maxWords
    Write-Host "[!] Ueber Ziel" -ForegroundColor Yellow
    Write-Host "    $diff Woerter zu viel" -ForegroundColor Yellow
}
else {
    Write-Host "[OK] Im Zielbereich!" -ForegroundColor Green
}

Write-Host ""

# Return word count for scripting
return $wordCount
