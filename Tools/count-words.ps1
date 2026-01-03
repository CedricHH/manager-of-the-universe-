# Word Counter für Kapitel
# Verwendung: .\count-words.ps1 "Pfad\zur\Datei.md"

param(
    [Parameter(Mandatory = $true)]
    [string]$FilePath
)

if (-not (Test-Path $FilePath)) {
    Write-Error "Datei nicht gefunden: $FilePath"
    exit 1
}

# Datei lesen
$content = Get-Content $FilePath -Raw -Encoding UTF8

# Speichere Original für Debug
$original = $content

# YAML-Frontmatter am Dateianfang entfernen (---...---)
# Nur wenn die Datei WIRKLICH mit --- beginnt (YAML-Style)
if ($content.TrimStart() -match '^---\s*\r?\n[\s\S]*?\r?\n---') {
    # Für echte YAML-Frontmatter
    $content = $content -replace '^\s*---\s*\r?\n[\s\S]*?\r?\n---\s*', ''
}

# Header-Metadaten entfernen (# Kapitel X: Titel, **POV**: etc.)
$lines = $content -split '\r?\n'
$filteredLines = @()
$inConsistencyCheck = $false

foreach ($line in $lines) {
    # Konsistenz-Check-Abschnitt erkennen und überspringen
    if ($line -match '^\s*##\s*KONSISTENZ-CHECK') {
        $inConsistencyCheck = $true
        continue
    }
    
    if ($inConsistencyCheck) {
        continue  # Alles nach KONSISTENZ-CHECK überspringen
    }
    
    # Metadaten-Zeilen überspringen
    if ($line -match '^\s*\*\*POV\*\*:' -or 
        $line -match '^\s*\*\*Ort\*\*:' -or 
        $line -match '^\s*\*\*Zeit\*\*:' -or 
        $line -match '^\s*\*\*Wortanzahl\*\*:') {
        continue
    }
    
    # "Ende Kapitel" Marker überspringen
    if ($line -match '^\s*\*Ende Kapitel') {
        continue
    }
    
    # Horizontale Linien (---) überspringen
    if ($line -match '^\s*---\s*$') {
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
$content = $content -replace '#+\s*', ''             # Headers (#, ##, etc.)
$content = $content -replace '\s+', ' '              # Normalize whitespace

# Wörter zählen (split by whitespace, filter empty)
$words = $content.Trim() -split '\s+' | Where-Object { $_.Length -gt 0 }
$wordCount = $words.Count

# Zeichen zählen (ohne Leerzeichen)
$charCount = ($content -replace '\s', '').Length

# Ausgabe
Write-Host ""
Write-Host "=== WORTANZAHL ===" -ForegroundColor Cyan
Write-Host "Datei: $(Split-Path $FilePath -Leaf)"
Write-Host ""
Write-Host "Woerter:   $wordCount" -ForegroundColor Green
Write-Host "Zeichen:   $charCount (ohne Leerzeichen)"
Write-Host ""

# Zielbereich-Check
if ($wordCount -lt 6000) {
    $diff = 6000 - $wordCount
    $percent = [math]::Round(($wordCount / 6000) * 100)
    Write-Host "[!] Unter Ziel (6.000-10.000)" -ForegroundColor Yellow
    Write-Host "    Noch ca. $diff Woerter bis Minimum ($percent%)" -ForegroundColor Yellow
}
elseif ($wordCount -gt 10000) {
    $diff = $wordCount - 10000
    Write-Host "[!] Ueber Ziel (6.000-10.000)" -ForegroundColor Yellow
    Write-Host "    Ca. $diff Woerter zu viel" -ForegroundColor Yellow
}
else {
    Write-Host "[OK] Im Zielbereich (6.000-10.000)" -ForegroundColor Green
}

Write-Host ""

# Return word count for scripting
return $wordCount
