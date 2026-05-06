$files = git ls-files --others --exclude-standard
foreach ($file in $files) {
    if ([string]::IsNullOrWhiteSpace($file)) { continue }
    Write-Host "Adding $file"
    git add $file
    git commit -m "Add $file"
    git push
    $delay = Get-Random -Minimum 120 -Maximum 300
    Write-Host "Waiting for $delay seconds before the next push..."
    Start-Sleep -Seconds $delay
}
Write-Host "Finished pushing all files!"
