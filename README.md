# BookMyShow Ticket Watcher (bms-watcher)

An automated monitoring tool built with Python, Playwright, and Telegram Bot API to watch ticket availability on BookMyShow for upcoming movies and venues, sending real-time notifications when bookings open.

## 🚀 Features

- **Automated Monitoring**: Periodically checks show listings for specified movies, venue codes, and region codes.
- **Playwright Support**: Handles dynamic pages and Cloudflare checks reliably using Playwright headless browser.
- **Telegram Alerts**: Sends instant alerts to your Telegram chat as soon as ticket bookings open.
- **GitHub Actions Integration**: Supports automated scheduled checks via GitHub Actions workflows without requiring a VPS.
- **Environment Configuration**: Configurable via `.env` file or environment variables.

## 📁 Project Structure

```
bms-watcher/
├── .github/
│   └── workflows/
│       └── watcher.yml
├── src/
│   ├── api.py           # BookMyShow API client
│   ├── config.py        # Environment & configuration loader
│   ├── logger.py        # Logging utility
│   ├── notifier.py      # Telegram notification service
│   ├── state.py         # State tracking (prevents duplicate alerts)
│   ├── utils.py         # Helper utilities
│   └── watcher.py       # Core ticket monitoring engine
├── .env.example         # Environment template
├── main.py              # Entry point script
├── requirements.txt     # Python dependencies
├── LICENSE              # Open source license
└── README.md            # Documentation
```

## 🛠️ Quick Start

### 1. Clone & Setup Environment

```bash
git clone https://github.com/gauthamram57/bms-watcher.git
cd bms-watcher
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
playwright install chromium
```

### 2. Configure Environment Variables

Copy `.env.example` to `.env` and fill in your details:

```bash
cp .env.example .env
```

Edit `.env`:
```env
TELEGRAM_BOT_TOKEN=your_bot_token_here
TELEGRAM_CHAT_ID=your_chat_id_here
MOVIE_NAME=Spider-Man: Brand New Day
VENUE_CODE=PBMC
REGION_CODE=COIM
DATE_CODE=20260729
CHECK_INTERVAL=300
```

### 3. Run the Watcher

```bash
python3 main.py
```

## 🤖 GitHub Actions Workflow

The project includes a GitHub Actions workflow in `.github/workflows/` that can automatically run the watcher on a schedule.

To set it up:
1. Go to repository **Settings > Secrets and variables > Actions**.
2. Add secrets for `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID`.
3. Enable GitHub Actions in the repository tab.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This project is intended for personal automation and educational purposes. It automates checking publicly accessible BookMyShow pages using a browser and sends notifications based on user-defined conditions. It is not affiliated with or endorsed by BookMyShow.
