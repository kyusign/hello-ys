import matplotlib.pyplot as plt
from .db import get_daily_views


def plot_views() -> None:
    rows = get_daily_views()
    if not rows:
        print("No data to plot")
        return
    dates = sorted(set(r["date"] for r in rows))
    platforms = sorted(set(r["platform"] for r in rows))
    data = {p: [0 for _ in dates] for p in platforms}
    idx = {d: i for i, d in enumerate(dates)}
    for r in rows:
        data[r["platform"]][idx[r["date"]]] = r["views"]
    for p, vals in data.items():
        plt.plot(dates, vals, label=p)
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
