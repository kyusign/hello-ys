import os
import sys
import time
import typer

if __package__ is None or __package__ == "":
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from sns_dashboard.gui import run as run_gui
from sns_dashboard.scheduler import start as start_scheduler
from sns_dashboard.viz import plot_views
from sns_dashboard.db import init_db
from sns_dashboard.config import load_config, config_exists, is_config_complete

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
    """Start scheduler for daily data fetch."""
    init_db()
    start_scheduler()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass


@app.command()
def plot() -> None:
    """Display a simple plot of collected views."""
    plot_views()


if __name__ == '__main__':
    if len(sys.argv) == 1:
        cfg = load_config() if config_exists() else None
        if cfg is None or not is_config_complete(cfg):
            # First run or incomplete config -> launch setup GUI
            sys.argv.append('setup')
        else:
            # Auto-start scheduler when configuration is present
            sys.argv.append('run')
    app()
