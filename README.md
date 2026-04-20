# Telegram File Uploader Bot

A safe and legitimate Telegram bot for handling user files. This bot demonstrates proper file handling practices using the official Telegram Bot API.

## Features

- ✅ Safe file handling with automatic cleanup
- 📁 Supports documents, photos, audio, voice messages, and videos
- 🔒 Uses official Telegram Bot API
- 🚀 Easy deployment on VPS, Heroku, and Google Colab
- 📝 Comprehensive logging

## Prerequisites

- Python 3.8+
- A Telegram Bot Token (get from [@BotFather](https://t.me/BotFather))

## Getting Your Bot Token

1. Open Telegram and search for [@BotFather](https://t.me/BotFather)
2. Send `/newbot` command
3. Follow the instructions to create your bot
4. Copy the API token provided

## Installation

### Clone the Repository

```bash
git clone <your-repo-url>
cd <repository-name>
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Set Environment Variable

```bash
export TELEGRAM_BOT_TOKEN="your_bot_token_here"
```

## Usage

Run the bot:

```bash
python bot.py
```

### Commands

- `/start` - Start the bot and see welcome message
- `/help` - Display help information

Simply send any file to the bot and it will process it safely and send it back.

## Deployment Guide

### Option 1: VPS Deployment (Ubuntu/Debian)

#### 1. Update System Packages

```bash
sudo apt update && sudo apt upgrade -y
```

#### 2. Install Python and pip

```bash
sudo apt install -y python3 python3-pip python3-venv git
```

#### 3. Clone Repository

```bash
git clone <your-repo-url>
cd <repository-name>
```

#### 4. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### 5. Set Environment Variable

Create a `.env` file:

```bash
echo "TELEGRAM_BOT_TOKEN=your_bot_token_here" > .env
```

Or export it:

```bash
export TELEGRAM_BOT_TOKEN="your_bot_token_here"
```

#### 6. Create Systemd Service

Create service file:

```bash
sudo nano /etc/systemd/system/telegram-bot.service
```

Add the following content:

```ini
[Unit]
Description=Telegram File Uploader Bot
After=network.target

[Service]
Type=simple
User=your_username
WorkingDirectory=/path/to/your/bot
Environment="TELEGRAM_BOT_TOKEN=your_bot_token_here"
ExecStart=/path/to/your/bot/venv/bin/python bot.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Replace `your_username` and paths accordingly.

#### 7. Enable and Start Service

```bash
sudo systemctl daemon-reload
sudo systemctl enable telegram-bot
sudo systemctl start telegram-bot
```

#### 8. Check Status

```bash
sudo systemctl status telegram-bot
```

View logs:

```bash
sudo journalctl -u telegram-bot -f
```

### Option 2: Heroku Deployment

#### 1. Install Heroku CLI

Download from: https://devcenter.heroku.com/articles/heroku-cli

#### 2. Login to Heroku

```bash
heroku login
```

#### 3. Create Heroku App

```bash
heroku create your-bot-name
```

#### 4. Create Procfile

Create a file named `Procfile` (no extension):

```
worker: python bot.py
```

#### 5. Create app.json (Optional)

Create `app.json`:

```json
{
  "name": "Telegram File Bot",
  "description": "A safe Telegram file uploader bot",
  "repository": "https://github.com/yourusername/your-repo",
  "keywords": ["telegram", "bot", "python"],
  "env": {
    "TELEGRAM_BOT_TOKEN": {
      "description": "Your Telegram Bot Token",
      "required": true
    }
  },
  "formation": {
    "worker": {
      "quantity": 1
    }
  }
}
```

#### 6. Set Environment Variable

```bash
heroku config:set TELEGRAM_BOT_TOKEN=your_bot_token_here
```

#### 7. Deploy to Heroku

```bash
git add .
git commit -m "Initial commit"
git push heroku main
```

#### 8. Check Logs

```bash
heroku logs --tail
```

#### 9. Scale Worker

```bash
heroku ps:scale worker=1
```

**Note:** Heroku free tier has been discontinued. You'll need a paid plan.

### Option 3: Google Colab (Temporary Testing)

Google Colab is not designed for running bots 24/7, but you can use it for testing:

#### 1. Open Google Colab

Go to: https://colab.research.google.com

#### 2. Create New Notebook

#### 3. Clone Repository

```python
!git clone <your-repo-url>
%cd <repository-name>
```

#### 4. Install Dependencies

```python
!pip install -r requirements.txt
```

#### 5. Set Environment Variable

```python
import os
os.environ['TELEGRAM_BOT_TOKEN'] = 'your_bot_token_here'
```

#### 6. Run the Bot

```python
!python bot.py
```

**Important:** The bot will stop when you close the Colab notebook or after ~12 hours of inactivity. Not suitable for production.

### Option 4: Docker Deployment

#### 1. Create Dockerfile

Create a `Dockerfile`:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV TELEGRAM_BOT_TOKEN=""

CMD ["python", "bot.py"]
```

#### 2. Build Docker Image

```bash
docker build -t telegram-bot .
```

#### 3. Run Container

```bash
docker run -d \
  --name telegram-bot \
  -e TELEGRAM_BOT_TOKEN=your_bot_token_here \
  telegram-bot
```

#### 4. Check Logs

```bash
docker logs -f telegram-bot
```

## Security Best Practices

1. **Never commit your bot token** to version control
2. Use environment variables for sensitive data
3. Keep dependencies updated
4. Monitor bot logs regularly
5. Implement rate limiting if needed
6. Validate file types and sizes

## Troubleshooting

### Bot doesn't respond

- Check if `TELEGRAM_BOT_TOKEN` is set correctly
- Verify the bot is not blocked by users
- Check logs for errors

### Import errors

- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Check Python version (3.8+)

### Connection issues

- Check your internet connection
- Verify firewall settings
- Ensure Telegram API is accessible

## License

This project is licensed under the MIT License.

## Disclaimer

This bot is designed for legitimate file handling purposes only. Users are responsible for ensuring they have the right to share any files they transmit through this bot. Do not use this bot to distribute copyrighted material without permission or for any illegal activities.

## Support

For issues and questions, please open an issue on the GitHub repository.
