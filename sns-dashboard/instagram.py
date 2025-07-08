"""Instagram Graph API helper."""

import requests

BASE_URL = "https://graph.facebook.com/v19.0"


def fetch_instagram_views(token: str):
    """Fetch recent media view counts."""
    url = f"{BASE_URL}/me/media?fields=id,caption,insights.metric(impressions)&access_token={token}"
    resp = requests.get(url)
    resp.raise_for_status()
    data = resp.json()
    results = []
    for item in data.get("data", []):
        media_id = item["id"]
        caption = item.get("caption", "")
        views = 0
        for insight in item.get("insights", {}).get("data", []):
            if insight.get("name") == "impressions":
                views = insight.get("values", [{}])[0].get("value", 0)
        results.append((media_id, caption, views))
    return results
