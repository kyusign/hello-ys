from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

from .fetchers.youtube import get_channel_views as youtube_views
from .fetchers.tiktok import get_channel_views as tiktok_views
from .fetchers.instagram import get_channel_views as instagram_views
from .db import insert_views

scheduler = BackgroundScheduler(timezone="Asia/Seoul")


def job_fetch_views() -> None:
    today = datetime.now().date().isoformat()
    print(f"Fetching views for {today}")
    insert_views("youtube", today, youtube_views())
    insert_views("tiktok", today, tiktok_views())
    insert_views("instagram", today, instagram_views())


def start() -> None:
    if not scheduler.get_job("daily_fetch"):
        scheduler.add_job(job_fetch_views, "cron", hour=0, id="daily_fetch")
    scheduler.start()
    print("Scheduler started. Running initial fetch...")
    job_fetch_views()
