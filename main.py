from telethon import TelegramClient
from telethon.tl.functions.account import UpdateStatusRequest
import logging
import asyncio
import os

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
)

# Configuration
api_id = int(os.getenv('TELEGRAM_API_ID', ''))
api_hash = os.getenv('TELEGRAM_API_HASH', '')
logfilename = 'log.csv'
delay_seconds = int(os.getenv('DELAY_SECONDS', '45'))

# Create Telegram client
client = TelegramClient('so', api_id, api_hash)

async def update_online_status():
    """Continuously update the online status and log the updates"""
    async with client:
        is_authorized = await client.is_user_authorized()
        if not is_authorized:
            logging.fatal("Login failed, please check your credentials.")
            return
        logging.info("You are now authorized. Starting to update online status.")
        while True:
            try:
                # Set status to online
                await client(UpdateStatusRequest(offline=False))
                logging.info("Updated online status successfully.")
            except Exception as e:
                logging.error(f"Failed to update online status: {str(e)}")
            # Delay between updates based on configuration
            logging.info(f"Sleeping for {delay_seconds} seconds.")
            await asyncio.sleep(delay_seconds)

if __name__ == "__main__":
    try:
        asyncio.run(update_online_status())
    except KeyboardInterrupt:
        logging.info("Script interrupted by user.")
