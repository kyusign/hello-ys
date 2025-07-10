import os
import sys
import typer

if __package__ is None or __package__ == "":
    # Adjust path so absolute imports work when running directly
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from sns_dashboard.gui import run as run_gui
from sns_dashboard.tasks import fetch_data
import time
from datetime import datetime, timedelta

app = typer.Typer(help='SNS Dashboard Command Line Interface')


@app.callback()
def main() -> None:
    """SNS Dashboard CLI."""
    pass


@app.command()
def setup() -> None:
    """Launch GUI setup window."""
    run_gui()


@app.command()
def run() -> None:
    """Fetch data every day at midnight."""
    while True:
        now = datetime.now()
        next_midnight = (now + timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
        time.sleep((next_midnight - now).total_seconds())
        fetch_data()


if __name__ == '__main__':
    if len(sys.argv) == 1:
        # Allow running `python sns_dashboard/main.py` directly
        # by defaulting to the setup command when no arguments are given.
        sys.argv.append('setup')
    app()
