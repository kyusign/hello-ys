import json
import os
from typing import Any, Dict

CONFIG_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.json")

DEFAULT_CONFIG = {
    "google_client_id": "",
    "google_client_secret": "",
    "instagram_client_id": "",
    "instagram_client_secret": "",
    "tiktok_client_key": "",
    "tiktok_client_secret": "",
    "spreadsheet_id": "",
    "youtube_url": "",
    "tiktok_url": "",
    "instagram_url": "",
    "rates": {
        "youtube": 0.0,
        "tiktok": 0.0,
        "instagram": 0.0,
    },
}


def config_exists() -> bool:
    """Return True if the configuration file exists."""
    return os.path.exists(CONFIG_PATH)


def is_config_complete(cfg: Dict[str, Any]) -> bool:
    required = [
        "google_client_id",
        "google_client_secret",
        "instagram_client_id",
        "instagram_client_secret",
        "tiktok_client_key",
        "tiktok_client_secret",
        "spreadsheet_id",
        "youtube_url",
        "tiktok_url",
        "instagram_url",
    ]
    return all(cfg.get(k) for k in required)


def load_config() -> Dict[str, Any]:
    if not os.path.exists(CONFIG_PATH):
        return DEFAULT_CONFIG.copy()
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def save_config(cfg: Dict[str, Any]) -> None:
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(cfg, f, indent=2)
