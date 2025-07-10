# SNS Dashboard

This project provides a simple GUI setup tool for storing API credentials for Google, Instagram, TikTok and a spreadsheet. The credentials are saved in `config.json` and can be used by other parts of the application.

## Usage

Install dependencies first:

```bash
pip install typer tkinter
```

To launch the GUI, run one of:

```bash
python -m sns_dashboard setup
```

or

```bash
python -m sns_dashboard.main setup
```

You can also execute the script directly:

```bash
python sns_dashboard/main.py setup
```

If packaged as an executable, you can invoke the setup with:

```bash
sns-dashboard.exe setup
```

Fill out each field in the window and press **Save**. The configuration will be written to `config.json` and an initial authentication step will run.
