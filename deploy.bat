@echo off
echo ========================================
echo   Super Ultimate Bot 3.0 - Deploy Script
echo ========================================
echo.

echo [1/3] Checking git status...
cd "C:\Users\admin\Desktop\bot\9app by zawng dep chai"
git status
echo.

echo [2/3] Adding all files to git...
git add .
echo.

echo [3/3] Committing changes...
git commit -m "Auto deploy - Super Ultimate Bot 3.0 - Multi-platform AI Integration"
echo.

echo ========================================
echo   Attempting to push to GitHub...
echo ========================================
git push origin main

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ========================================
    echo   SUCCESS! Code pushed to GitHub
    echo ========================================
    echo.
    echo Next steps:
    echo 1. Go to https://render.com
    echo 2. Click New -^> Web Service
    echo 3. Connect your GitHub repository
    echo 4. Add environment variables:
    echo    - DISCORD_TOKEN
    echo    - ADMIN_IDS
    echo 5. Click Deploy
) else (
    echo.
    echo ========================================
    echo   ERROR! Failed to push to GitHub
    echo ========================================
    echo.
    echo Possible solutions:
    echo 1. Check your GitHub permissions
    echo 2. Create a new repository
    echo 3. Update git remote URL
    echo See DEPLOY_GUIDE.md for detailed instructions
)

echo.
pause