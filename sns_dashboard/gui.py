import tkinter as tk
from tkinter import messagebox

from .config import load_config, save_config


class SetupGUI:
    def __init__(self, master: tk.Tk):
        self.master = master
        master.title("SNS Dashboard Setup")

        self.entries: dict[str, tk.Entry] = {}

        # (라벨, 설정키) 튜플 ― URL 3개 + CPM 3개
        fields = [
            ("YouTube Channel URL", "youtube_url"),
            ("TikTok Channel URL", "tiktok_url"),
            ("Instagram Channel URL", "instagram_url"),
            ("YouTube CPM", "rate_youtube"),
            ("TikTok CPM", "rate_tiktok"),
            ("Instagram CPM", "rate_instagram"),
        ]

        for i, (label, key) in enumerate(fields):
            tk.Label(master, text=label).grid(row=i, column=0, sticky="e", pady=2, padx=2)
            entry = tk.Entry(master, width=45)
            entry.grid(row=i, column=1, pady=2, padx=2)
            self.entries[key] = entry

        tk.Button(master, text="Save", command=self.save).grid(
            row=len(fields), column=0, columnspan=2, pady=10
        )

        self.load_existing()

    def load_existing(self) -> None:
        data = load_config()
        for key, entry in self.entries.items():
            if key.startswith("rate_"):
                platform = key.split("_", 1)[1]
                value = data.get("rates", {}).get(platform)
            else:
                value = data.get(key)
            if value is not None:
                entry.delete(0, tk.END)
                entry.insert(0, str(value))

    def save(self) -> None:
        data = load_config()

        # URL 저장
        for key in ["youtube_url", "tiktok_url", "instagram_url"]:
            data[key] = self.entries[key].get().strip()

        # CPM 저장
        rates = data.get("rates", {})
        rates["youtube"] = float(self.entries["rate_youtube"].get() or 0)
        rates["tiktok"] = float(self.entries["rate_tiktok"].get() or 0)
        rates["instagram"] = float(self.entries["rate_instagram"].get() or 0)
        data["rates"] = rates

        save_config(data)
        messagebox.showinfo("Saved", "Configuration saved.")


def run() -> None:
    root = tk.Tk()
    SetupGUI(root)
    root.mainloop()


if __name__ == "__main__":
    run()
