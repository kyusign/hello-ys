"""OAuth helper functions for Google, Instagram and TikTok."""

import json
import os
import webbrowser
from flask import Flask, request
from google_auth_oauthlib.flow import InstalledAppFlow

CRED_PATH = os.path.expanduser("~/.sns_dash/creds.json")

app = Flask(__name__)

@app.route("/callback")
def callback():
    code = request.args.get("code")
    return "Authentication complete. You can close this window."  # Browser shows this


def start_local_http_server(port: int = 8080):
    """Start a local server to receive OAuth redirect."""
    app.run(port=port)


def get_token(scopes):
    """Perform OAuth desktop flow and store credentials."""
    flow = InstalledAppFlow.from_client_secrets_file("config.json", scopes=scopes)
    creds = flow.run_local_server(port=0)
    os.makedirs(os.path.dirname(CRED_PATH), exist_ok=True)
    with open(CRED_PATH, "w") as f:
        f.write(creds.to_json())
    return creds
