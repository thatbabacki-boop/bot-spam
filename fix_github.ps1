# GitHub Remote Fix Script
# Change this to your GitHub username and repository name
$GITHUB_USERNAME = "YOUR_USERNAME"
$REPO_NAME = "super-ultimate-bot-3"

Write-Host "========================================"  -ForegroundColor Cyan
Write-Host "  GitHub Remote Configuration"  -ForegroundColor Cyan  
Write-Host "========================================"  -ForegroundColor Cyan
Write-Host ""

# Navigate to project directory
Set-Location "C:\Users\admin\Desktop\bot\9app by zawng dep chai"

# Show current remote
Write-Host "[Current Remote Configuration]" -ForegroundColor Yellow
git remote -v
Write-Host ""

# Check if user wants to continue
if ($GITHUB_USERNAME -eq "YOUR_USERNAME") {
    Write-Host "ERROR: Please edit this script and set your GitHub username!" -ForegroundColor Red
    Write-Host "Change line 3: `$GITHUB_USERNAME = `"YOUR_USERNAME`"" -ForegroundColor Yellow
    pause
    exit
}

# New remote URL
$newRemote = "https://github.com/$GITHUB_USERNAME/$REPO_NAME.git"

Write-Host "[New Remote Configuration]" -ForegroundColor Green
Write-Host "URL: $newRemote" -ForegroundColor White
Write-Host ""

# Ask for confirmation
$confirmation = Read-Host "Do you want to change the remote URL? (y/n)"
if ($confirmation -eq 'y' -or $confirmation -eq 'Y') {
    # Change remote URL
    git remote set-url origin $newRemote
    
    Write-Host "[Remote Updated Successfully]" -ForegroundColor Green
    git remote -v
    Write-Host ""
    
    # Push to new remote
    Write-Host "[Pushing to New Remote]" -ForegroundColor Yellow
    git push origin main
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host ""
        Write-Host "========================================"  -ForegroundColor Green
        Write-Host "  SUCCESS! Code pushed to GitHub"  -ForegroundColor Green
        Write-Host "========================================"  -ForegroundColor Green
        Write-Host ""
        Write-Host "Next steps:" -ForegroundColor Cyan
        Write-Host "1. Go to https://render.com" -ForegroundColor White
        Write-Host "2. Create Web Service with your GitHub repo" -ForegroundColor White
        Write-Host "3. Add environment variables" -ForegroundColor White
        Write-Host "4. Deploy!" -ForegroundColor White
    } else {
        Write-Host ""
        Write-Host "ERROR: Push failed. Check your GitHub credentials." -ForegroundColor Red
    }
} else {
    Write-Host "Operation cancelled by user." -ForegroundColor Yellow
}

Write-Host ""
pause