# SNS Dashboard

This project is a simple prototype for a desktop application that collects
view counts from YouTube, Instagram and TikTok and stores them in a Google
Sheet. It follows the design from the previous discussion.

## Setup

1. Install dependencies:
   ```bash
   python -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt
   ```
2. Create `config.json` with your OAuth credentials.
3. Run `python main.py init` to authenticate.
4. Run `python main.py update` to fetch data.

The project can be packaged using PyInstaller via `build.bat`.
