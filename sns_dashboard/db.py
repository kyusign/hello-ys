import os
import sqlite3
from typing import Iterable, Tuple

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data.db")

SCHEMA = """
CREATE TABLE IF NOT EXISTS channels (
    platform TEXT PRIMARY KEY,
    url TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS rates (
    platform TEXT PRIMARY KEY,
    cpm REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS views (
    platform TEXT,
    date DATE,
    views INTEGER,
    PRIMARY KEY(platform, date)
);

CREATE VIEW IF NOT EXISTS earnings AS
SELECT v.platform,
       v.date,
       v.views,
       ROUND(v.views / 1000.0 * r.cpm, 2) AS revenue
FROM   views v
JOIN   rates r USING(platform);

CREATE VIEW IF NOT EXISTS views_monthly AS
SELECT platform,
       substr(date, 1, 7) AS yyyymm,
       SUM(views) AS views_month
FROM views
GROUP BY platform, yyyymm;

CREATE VIEW IF NOT EXISTS earnings_monthly AS
SELECT v.platform,
       v.yyyymm,
       v.views_month,
       ROUND(v.views_month / 1000.0 * r.cpm, 2) AS revenue_month
FROM views_monthly v
JOIN rates r USING(platform);
"""


def get_conn() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    conn = get_conn()
    conn.executescript(SCHEMA)
    conn.commit()


def insert_views(platform: str, date: str, views: int) -> None:
    conn = get_conn()
    conn.execute(
        "INSERT OR REPLACE INTO views(platform, date, views) VALUES (?, ?, ?)",
        (platform, date, views),
    )
    conn.commit()


def get_daily_views() -> Iterable[Tuple[str, str, int]]:
    conn = get_conn()
    return conn.execute("SELECT platform, date, views FROM views ORDER BY date").fetchall()
