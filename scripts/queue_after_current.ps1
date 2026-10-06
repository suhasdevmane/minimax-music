# Wait for the currently running render queue to finish, then start another.
# Usage (detached):
#   Start-Process pwsh -ArgumentList "-File scripts\queue_after_current.ps1 02-... 03-... 05-..."
param([Parameter(ValueFromRemainingArguments = $true)][string[]]$Songs)

$root = Split-Path -Parent $PSScriptRoot
$status = Join-Path $root "render_queue.status"

Add-Content $status ("{0} CHAIN_WAITING for current queue, then: {1}" -f (Get-Date -Format "yyyy-MM-dd HH:mm:ss"), ($Songs -join " "))

while ($true) {
    $last = Get-Content $status -Tail 1 -ErrorAction SilentlyContinue
    if ($last -match "QUEUE_COMPLETE") { break }
    Start-Sleep -Seconds 60
}

Start-Sleep -Seconds 10   # let the previous runner exit and release the GPU
Add-Content $status ("{0} CHAIN_STARTING {1}" -f (Get-Date -Format "yyyy-MM-dd HH:mm:ss"), ($Songs -join " "))

$py = Join-Path $root ".venv\Scripts\python.exe"
$runner = Join-Path $root "scripts\render_queue.py"
Start-Process -FilePath $py -ArgumentList (@("-u", $runner) + $Songs) -WorkingDirectory $root -WindowStyle Hidden `
    -RedirectStandardOutput (Join-Path $root "render_queue.out.log") -RedirectStandardError (Join-Path $root "render_queue.err.log")
