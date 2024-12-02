# StayOnline-Telegram

**A tool to keep your Telegram status always online.**  

## Installation 

1. Clone the repository:  
   ```bash
   git clone https://github.com/Miyuu233/StayOnline-Telegram.git
   cd StayOnline-Telegram
   ```  

2. Install dependencies:  
   ```bash
   pip3 install telethon
   ```  

3. Set up environment variables for API credentials:  
   ```bash
   export TELEGRAM_API_ID=your_api_id
   export TELEGRAM_API_HASH=your_api_hash
   ```  
4. (Optional) Configure delay for refreshing online status:
Set the DELAY_SECONDS environment variable to customize the delay (default is 45 seconds):
   ```bash
   export DELAY_SECONDS=15
   ```
   
---

## Usage

1. Run the script:  
   ```bash
   python3 main.py
   ```  

2. The bot will keep your Telegram status online and log all updates to a `log.csv` file.
