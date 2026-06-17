import os
import sys
import io

# Set UTF-8 encoding for stdout
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

print("Super Ultimate Bot 3.0 - Starting...")
print("Multi-platform | AI Integration | Optimized Performance")
print("-" * 50)

# Check for environment variables
if os.environ.get("DISCORD_TOKEN"):
    print("DISCORD_TOKEN found in environment variables")
else:
    print("ERROR: DISCORD_TOKEN not set in environment variables")
    print("Please set DISCORD_TOKEN environment variable or run with input")
    sys.exit(1)

if os.environ.get("ADMIN_IDS"):
    print("ADMIN_IDS found in environment variables")
else:
    print("ERROR: ADMIN_IDS not set in environment variables")
    print("Please set ADMIN_IDS environment variable or run with input")
    sys.exit(1)

print("-" * 50)
print("Initializing bot systems...")
print("Loading modules...")
print("Preparing AI integration...")
print("Connecting to Discord...")

# Now import and run the bot
import bot