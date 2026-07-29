# BookMyShow Watcher

A lightweight, configurable BookMyShow booking watcher built with Python and Playwright. Monitor any BookMyShow booking page and receive an instant Telegram notification when bookings become available.

## Features

- Monitor any BookMyShow booking page
- Uses Playwright to handle Cloudflare-protected pages
- Sends instant Telegram notifications
- Runs automatically every 5 minutes using GitHub Actions
- Lightweight and easy to configure
- Works for any city, cinema, or event available on BookMyShow

---

## How It Works

The watcher periodically opens a BookMyShow booking page using a Chromium browser.

When the page becomes available (or matches your configured condition), it sends a Telegram notification.

This approach monitors the same booking page that users access in their browsers instead of relying on undocumented APIs.

---

## Tech Stack

- Python 3
- Playwright
- Requests
- GitHub Actions
- Telegram Bot API

---

## Project Structure

```
bms-watcher/
├── .github/
│   └── workflows/
│       └── watcher.yml
├── main.py
├── watcher.py
├── notifier.py
├── config.py
├── requirements.txt
├── .env.example
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/bms-watcher.git
cd bms-watcher
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

**Linux/macOS**

```bash
source venv/bin/activate
```

**Windows**

```powershell
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
playwright install chromium
```

Run the watcher:

```bash
python main.py
```

---

## Configuration

Configure the watcher by editing `config.py` or using environment variables.

Example:

```python
BOOKING_URL = "https://in.bookmyshow.com/cinemas/..."
CHECK_INTERVAL = 300
```

---

## Telegram Setup

1. Create a bot using `@BotFather`.
2. Copy the bot token.
3. Obtain your Telegram Chat ID.
4. Add them as environment variables or GitHub Secrets.

Required values:

```
BOT_TOKEN
CHAT_ID
```

---

## GitHub Actions

The project includes a GitHub Actions workflow that checks the configured booking page every five minutes.

Setup:

1. Fork or clone the repository.
2. Add the required GitHub Secrets.
3. Enable GitHub Actions.

No server or VPS is required.

---

## Use Cases

- Movie ticket releases
- Early booking notifications
- Special screenings
- Limited-release events
- Popular shows
- Any publicly accessible BookMyShow booking page

---

## Example Notification

```
Booking Alert

The monitored BookMyShow page is now available.

https://in.bookmyshow.com/...
```

---

## Roadmap

- Multiple booking page support
- Discord notifications
- Email notifications
- Slack integration
- Multiple cinema monitoring
- Docker support
- YAML configuration
- Retry handling and health logging

---

## Contributing

Contributions are welcome. Feel free to open an issue or submit a pull request.

---

## License

This project is licensed under the MIT License.

---

## Disclaimer

This project is intended for personal automation and educational purposes. It automates checking publicly accessible BookMyShow pages using a browser and sends notifications based on user-defined conditions. It is not affiliated with or endorsed by BookMyShow.