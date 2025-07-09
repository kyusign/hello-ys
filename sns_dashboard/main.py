import typer

from .gui import run as run_gui

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
    app()
