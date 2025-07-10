# SNS Dashboard

This project collects daily view counts from YouTube, TikTok and Instagram channels and computes estimated revenue. Credentials and channel information are stored in `config.json` through a small Tkinter GUI.

## Usage

Install dependencies first:

```bash
pip install typer apscheduler matplotlib tkinter
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

Running `python sns_dashboard/main.py` without any arguments will launch the setup window on first run. If `config.json` already exists and is filled out, the scheduler starts automatically instead.

If packaged as an executable, you can invoke the setup with:

```bash
sns-dashboard.exe setup
```

Fill out each field in the window and press **Save**. The configuration will be written to `config.json` and an initial authentication step will run. Fields include API credentials, channel URLs and CPM rates for each platform.

## Scheduled Data Collection

After completing the setup you can start a background process that collects data each day at midnight:

```bash
python -m sns_dashboard run
```

This command initializes the SQLite database and schedules a fetch job every day at 00:00.

If the configuration file already exists, you can simply run:

```bash
python -m sns_dashboard
```

or run the packaged executable to start the scheduler immediately.

Collected data can be visualized with:

```bash
python -m sns_dashboard plot
```
