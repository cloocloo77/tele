<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python Version">
  <img src="https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/badge/Telegram-Bot-orange?style=for-the-badge&logo=telegram" alt="Telegram Bot">
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge" alt="Status">
</p>

<h1 align="center">🤖 Telegram File Uploader Bot</h1>

<p align="center">
  <strong>A professional, secure, and versatile Telegram bot for safe file handling</strong>
</p>

<p align="center">
  <a href="#features">Features</a> •
  <a href="#quick-start">Quick Start</a> •
  <a href="#deployment">Deployment</a> •
  <a href="#configuration">Configuration</a> •
  <a href="#security">Security</a> •
  <a href="#troubleshooting">Troubleshooting</a>
</p>

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 📁 **Multi-Format Support** | Documents, Photos, Audio, Voice Messages, Videos |
| 🔒 **Secure Handling** | Automatic file cleanup and secure temporary storage |
| 🚀 **Multi-Platform** | Deploy on VPS, Heroku, Google Colab, or Docker |
| 📊 **Detailed Logging** | Comprehensive logs for monitoring and debugging |
| ⚡ **High Performance** | Async operations for efficient file processing |
| 🛡️ **Official API** | Built with python-telegram-bot using official Telegram Bot API |

---

## 🚀 Quick Start

### 1. Get Your Bot Token

<details>
<summary>Click to expand instructions</summary>

1. Open Telegram and search for [@BotFather](https://t.me/BotFather)
2. Send `/newbot` command
3. Choose a name and username for your bot
4. Copy the API token provided (looks like: `1234567890:ABCdefGHIjklMNOpqrsTUVwxyz`)

</details>

### 2. Install & Run

```bash
# Clone the repository
git clone https://github.com/cloocloo77/tele.git
cd tele

# Install dependencies
pip install -r requirements.txt

# Set your bot token
export TELEGRAM_BOT_TOKEN="your_bot_token_here"

# Run the bot
python bot.py
```

---

## 🌐 Deployment

<details open>
<summary><h3>🖥️ Option 1: VPS (Ubuntu/Debian) - Recommended for 24/7</h3></summary>

#### Step-by-Step Setup

```bash
# 1. Update system
sudo apt update && sudo apt upgrade -y

# 2. Install Python & dependencies
sudo apt install -y python3 python3-pip python3-venv git

# 3. Clone and setup
git clone https://github.com/cloocloo77/tele.git
cd tele
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 4. Create environment file
echo "TELEGRAM_BOT_TOKEN=your_token_here" > .env

# 5. Create systemd service
sudo tee /etc/systemd/system/telegram-bot.service > /dev/null <<EOF
[Unit]
Description=Telegram File Uploader Bot
After=network.target

[Service]
Type=simple
User=$USER
WorkingDirectory=$(pwd)
Environment="TELEGRAM_BOT_TOKEN=your_token_here"
ExecStart=$(pwd)/venv/bin/python bot.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF

# 6. Enable and start
sudo systemctl daemon-reload
sudo systemctl enable telegram-bot
sudo systemctl start telegram-bot

# 7. Check status
sudo systemctl status telegram-bot
```

**Useful Commands:**
- View logs: `sudo journalctl -u telegram-bot -f`
- Stop bot: `sudo systemctl stop telegram-bot`
- Restart bot: `sudo systemctl restart telegram-bot`

</details>

<details>
<summary><h3>☁️ Option 2: Heroku - Cloud Platform</h3></summary>

> ⚠️ **Note:** Heroku free tier discontinued. Paid plan required.

```bash
# 1. Login to Heroku
heroku login

# 2. Create app
heroku create your-bot-name

# 3. Set environment variable
heroku config:set TELEGRAM_BOT_TOKEN=your_token_here

# 4. Deploy
git push heroku main

# 5. Scale worker
heroku ps:scale worker=1

# 6. View logs
heroku logs --tail
```

**Required Files:** `Procfile` and `app.json` are included in this repo.

</details>

<details>
<summary><h3>📓 Option 3: Google Colab - Testing Only</h3></summary>

> ⚠️ **Warning:** Not for production. Session expires after ~12 hours.

```python
# In Colab notebook cell 1
!git clone https://github.com/cloocloo77/tele.git
%cd tele
!pip install -r requirements.txt

# In cell 2
import os
os.environ['TELEGRAM_BOT_TOKEN'] = 'your_token_here'

# In cell 3
!python bot.py
```

</details>

<details>
<summary><h3>🐳 Option 4: Docker - Containerized</h3></summary>

```bash
# Build image
docker build -t telegram-bot .

# Run container
docker run -d \
  --name telegram-bot \
  -e TELEGRAM_BOT_TOKEN=your_token_here \
  --restart unless-stopped \
  telegram-bot

# View logs
docker logs -f telegram-bot
```

</details>

---

## ⚙️ Configuration

| Environment Variable | Required | Description | Example |
|---------------------|----------|-------------|---------|
| `TELEGRAM_BOT_TOKEN` | ✅ Yes | Your bot token from BotFather | `123456:ABC-DEF1234...` |

---

## 🛡️ Security Best Practices

<div align="center">

| ✅ Do | ❌ Don't |
|-------|----------|
| Use environment variables | Hardcode tokens in code |
| Keep dependencies updated | Ignore security updates |
| Monitor logs regularly | Share bot tokens publicly |
| Validate file types | Allow unlimited file sizes |
| Use HTTPS for webhooks | Use HTTP for sensitive data |

</div>

---

## 🔧 Troubleshooting

| Issue | Solution |
|-------|----------|
| Bot doesn't respond | Verify token is correct and bot isn't blocked |
| Import errors | Run `pip install -r requirements.txt` |
| Connection timeout | Check firewall and internet connection |
| Permission denied | Ensure execute permissions on scripts |

**Enable Debug Mode:**
```bash
export PYTHONDEBUG=1
python bot.py
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

## ⚠️ Disclaimer

> This bot is designed for **legitimate file handling purposes only**. Users are responsible for ensuring they have the right to share any files transmitted through this bot. Do not use this bot to distribute copyrighted material without permission or for any illegal activities.

---

<p align="center">
  <strong>Made with ❤️ for the Telegram community</strong>
</p>

<p align="center">
  <a href="https://github.com/cloocloo77/tele/issues">Report Bug</a> •
  <a href="https://github.com/cloocloo77/tele/issues">Request Feature</a> •
  <a href="https://github.com/cloocloo77/tele">Star this Repo</a>
</p>
