"""YouTube API helper."""

from googleapiclient.discovery import build


def fetch_youtube_stats(channel_url: str, creds):
    """Fetch video IDs and view counts for a channel."""
    youtube = build("youtube", "v3", credentials=creds)
    # Example simple fetch of uploads playlist
    channel_id = channel_url.split("/")[-1]
    req = youtube.channels().list(part="contentDetails", id=channel_id)
    res = req.execute()
    uploads_id = res["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]
    videos_req = youtube.playlistItems().list(part="snippet", playlistId=uploads_id, maxResults=5)
    videos_res = videos_req.execute()
    results = []
    for item in videos_res.get("items", []):
        vid = item["snippet"]["resourceId"]["videoId"]
        stats = youtube.videos().list(part="statistics,snippet", id=vid).execute()
        views = stats["items"][0]["statistics"].get("viewCount")
        title = stats["items"][0]["snippet"].get("title")
        results.append((vid, title, views))
    return results
