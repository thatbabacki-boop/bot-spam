import os
import sys

# Set environment variables if not already set
if not os.environ.get("DISCORD_TOKEN"):
    token = input("   Token bot: ").strip()
    os.environ["DISCORD_TOKEN"] = token

if not os.environ.get("ADMIN_IDS"):
    admin_ids = input("   ID Admin: ").strip()
    os.environ["ADMIN_IDS"] = admin_ids

# Now import and run the bot
import bot