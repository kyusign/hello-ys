"""CLI entry point using Typer."""

import json
import typer

from auth import get_token
from youtube import fetch_youtube_stats
from instagram import fetch_instagram_views
from tiktok import fetch_tiktok_views
from sheets import append_rows

app = typer.Typer()

CONFIG_FILE = "config.json"


def load_config():
    with open(CONFIG_FILE) as f:
        return json.load(f)


@app.command()
def init():
    """Authenticate and store credentials."""
    config = load_config()
    scopes = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/youtube.readonly"]
    creds = get_token(scopes)
    typer.echo("Authentication successful")


@app.command()
def update(channel_url: str):
    """Fetch stats and update sheet."""
    config = load_config()
    creds = get_token([])  # load stored
    yt_data = fetch_youtube_stats(channel_url, creds)
    rows = [[title, views] for _, title, views in yt_data]
    append_rows(config["spreadsheet_id"], rows, creds)
    typer.echo("Sheet updated")


if __name__ == "__main__":
    app()
