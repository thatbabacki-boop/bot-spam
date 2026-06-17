#!/usr/bin/env python3
"""
Health check endpoint for Render deployment
This simple script checks if the bot environment is properly configured
"""

import os
import sys

def check_health():
    """Check if required environment variables are set"""
    checks = {
        "DISCORD_TOKEN": os.environ.get("DISCORD_TOKEN"),
        "ADMIN_IDS": os.environ.get("ADMIN_IDS"),
    }
    
    all_good = True
    for key, value in checks.items():
        if value:
            print(f"✅ {key}: Set")
        else:
            print(f"❌ {key}: Not set")
            all_good = False
    
    if all_good:
        print("✅ All checks passed - Bot is healthy")
        return 0
    else:
        print("❌ Some checks failed - Bot is not healthy")
        return 1

if __name__ == "__main__":
    sys.exit(check_health())