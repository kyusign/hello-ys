from .db import get_conn


def update_today() -> None:
    # Simple calculation using views and rates tables
    conn = get_conn()
    conn.execute(
        "INSERT OR REPLACE INTO earnings SELECT v.platform, v.date, v.views, ROUND(v.views / 1000.0 * r.cpm, 2) FROM views v JOIN rates r USING(platform)"
    )
    conn.commit()
