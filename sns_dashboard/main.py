import os
import sys
import typer

if __package__ is None or __package__ == "":
    # Adjust path so absolute imports work when running directly
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from sns_dashboard.gui import run as run_gui

app = typer.Typer(help='SNS Dashboard Command Line Interface')


@app.callback()
def main() -> None:
    """SNS Dashboard CLI."""
    pass


@app.command()
def setup() -> None:
    """Launch GUI setup window."""
    run_gui()


if __name__ == '__main__':
    if len(sys.argv) == 1:
        # Allow running `python sns_dashboard/main.py` directly
        # by defaulting to the setup command when no arguments are given.
        sys.argv.append('setup')
    app()
