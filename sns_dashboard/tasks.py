from datetime import datetime

from .scheduler import job_fetch_views


def fetch_data() -> None:
    """Run a single data fetch immediately."""
    print(f"Manual fetch at {datetime.now().isoformat()}")
    job_fetch_views()

