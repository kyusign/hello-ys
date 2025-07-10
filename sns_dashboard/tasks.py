from datetime import datetime

from .scheduler import job_fetch_views
from .db import init_db


def fetch_data() -> None:
    """Run a single data fetch immediately."""
    print(f"Manual fetch at {datetime.now().isoformat()}")
    init_db()
    job_fetch_views()

