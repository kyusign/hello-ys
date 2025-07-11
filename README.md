# SNS Dashboard

This project collects daily view counts from YouTube, TikTok and Instagram channels and computes estimated revenue. A small Tkinter GUI lets you enter API credentials, channel URLs and CPM rates which are saved to `config.json`.

## Usage

Install dependencies first:

```bash
pip install -r requirements.txt
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

Running `python sns_dashboard/main.py` without any arguments will launch the setup window on first run. If `config.json` already exists and is filled out, the scheduler starts automatically instead. You can also run `python -m sns_dashboard` for the same behavior.

If packaged as an executable, you can invoke the setup with:

```bash
sns-dashboard.exe setup
```

Fill in each credential field along with the three channel URLs and optional CPM rates, then press **Save**. The configuration will be written to `config.json` and an initial authentication step will run.

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
