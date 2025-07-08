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
2. Create `config.json` with your OAuth credentials. Example:
   ```json
   {
     "google_client_id": "<YOUR_GOOGLE_CLIENT_ID>",
     "google_client_secret": "<YOUR_GOOGLE_CLIENT_SECRET>",
     "instagram_client_id": "<YOUR_INSTAGRAM_CLIENT_ID>",
     "instagram_client_secret": "<YOUR_INSTAGRAM_CLIENT_SECRET>",
     "tiktok_client_key": "<YOUR_TIKTOK_CLIENT_KEY>",
     "tiktok_client_secret": "<YOUR_TIKTOK_CLIENT_SECRET>",
     "spreadsheet_id": "<TARGET_SHEET_ID>"
   }
   ```
3. Run `python main.py init` to authenticate and store tokens.
4. Run `python main.py update --channel-url <YouTube_Channel_URL>` to fetch
   statistics and append them to the Google Sheet.

### Packaging the app

If you need a standalone Windows executable, run `build.bat`. The resulting
`sns-dashboard.exe` will appear in the `dist/` directory and can be executed in
place. Use it the same way as the Python scripts:

```cmd
sns-dashboard.exe init
sns-dashboard.exe update --channel-url <YouTube_Channel_URL>
```
