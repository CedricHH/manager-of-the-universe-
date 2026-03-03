param(
    [int]$StartChapter = 16,
    [int]$EndChapter = 116
)

$chaptersPath = "g:\Meine Ablage\EBOOKS\Der Manager des Universums\Story\Chapters"
$toolsPath = "g:\Meine Ablage\EBOOKS\Der Manager des Universums\Tools"

# Get all chapter files sorted by number
$allChapters = Get-ChildItem -Path "$chaptersPath\Chapter_*.md" | 
    Where-Object { $_.Name -notmatch '\(1\)' } | 
    Sort-Object { [int]($_.Name -replace 'Chapter_(\d+)_.*','$1') }

# Build lookup table for next chapter titles
$chapterLookup = @{}
foreach ($ch in $allChapters) {
    $num = [int]($ch.Name -replace 'Chapter_(\d+)_.*','$1')
    $title = ($ch.Name -replace 'Chapter_\d+_','').Replace('.md','').Replace('_',' ')
    $chapterLookup[$num] = @{
        Title = $title
        Path = $ch.FullName
        Name = $ch.Name
    }
}

$results = @()

foreach ($ch in $allChapters) {
    $num = [int]($ch.Name -replace 'Chapter_(\d+)_.*','$1')
    
    if ($num -lt $StartChapter -or $num -gt $EndChapter) { continue }
    
    $content = Get-Content $ch.FullName -Raw
    
    # Check if footer already exists
    if ($content -match '\*\*Word Count\*\*:') {
        Write-Host "[$num] Already has footer, skipping: $($ch.Name)" -ForegroundColor Yellow
        continue
    }
    
    # Get word count using the tool
    $wordCountOutput = & "$toolsPath\count-words.bat" $ch.FullName 2>&1
    $wordCount = ($wordCountOutput | Select-String "Woerter:\s+(\d+)" | ForEach-Object { $_.Matches.Groups[1].Value })
    
    if (-not $wordCount) {
        Write-Host "[$num] Could not get word count for: $($ch.Name)" -ForegroundColor Red
        continue
    }
    
    # Get next chapter title
    $nextNum = $num + 1
    $nextTitle = if ($chapterLookup.ContainsKey($nextNum)) { $chapterLookup[$nextNum].Title } else { "TBD" }
    
    # Create footer
    $footer = @"

---

**Word Count**: $wordCount
**Next Chapter**: [$nextTitle]
"@
    
    # Append footer to file
    Add-Content -Path $ch.FullName -Value $footer -NoNewline
    
    Write-Host "[$num] Added footer: $wordCount words, next: $nextTitle" -ForegroundColor Green
    
    $results += [PSCustomObject]@{
        Chapter = $num
        WordCount = $wordCount
        NextChapter = $nextTitle
    }
}

Write-Host "`n=== Summary ===" -ForegroundColor Cyan
Write-Host "Processed: $($results.Count) chapters"
$results | Format-Table -AutoSize
