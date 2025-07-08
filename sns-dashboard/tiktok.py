"""TikTok Open API helper."""

import requests

BASE_URL = "https://open.tiktokapis.com/v1"


def fetch_tiktok_views(token: str):
    """Fetch recent video view counts."""
    headers = {"Authorization": f"Bearer {token}"}
    url = f"{BASE_URL}/video/list"  # Placeholder endpoint
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    data = resp.json()
    results = []
    for item in data.get("data", []):
        vid = item.get("id")
        title = item.get("title", "")
        views = item.get("stats", {}).get("playCount")
        results.append((vid, title, views))
    return results
