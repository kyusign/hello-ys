import json
import os
import tkinter as tk
from tkinter import messagebox

from .auth import get_token
from .config import load_config, save_config


class SetupGUI:
    def __init__(self, master: tk.Tk):
        self.master = master
        master.title("SNS Dashboard Setup")

        self.entries: dict[str, tk.Entry] = {}

        # (라벨, 설정키) 튜플
        fields = [
            ("Google Client ID", "google_client_id"),
            ("Google Client Secret", "google_client_secret"),
            ("Instagram Client ID", "instagram_client_id"),
            ("Instagram Client Secret", "instagram_client_secret"),
            ("TikTok Client Key", "tiktok_client_key"),
            ("TikTok Client Secret", "tiktok_client_secret"),
            ("Spreadsheet ID", "spreadsheet_id"),
            ("YouTube Channel URL", "youtube_url"),
            ("TikTok Channel URL", "tiktok_url"),
            ("Instagram Channel URL", "instagram_url"),
            ("YouTube CPM", "rate_youtube"),
            ("TikTok CPM", "rate_tiktok"),
            ("Instagram CPM", "rate_instagram"),
        ]

        # 위젯 생성
        for i, (label_text, key) in enumerate(fields):
            tk.Label(master, text=label_text).grid(row=i, column=0, sticky="e", pady=2, padx=2)
            entry = tk.Entry(master, width=45)
            entry.grid(row=i, column=1, pady=2, padx=2)
            self.entries[key] = entry

        tk.Button(master, text="Save", command=self.save).grid(
            row=len(fields), column=0, columnspan=2, pady=10
        )

        self.load_existing()

    # 기존 config.json 값 채워 넣기
    def load_existing(self) -> None:
        data = load_config()  # 파일 없으면 {} 반환
        for key, entry in self.entries.items():
            if key.startswith("rate_"):
                platform = key.split("_", 1)[1]
                value = data.get("rates", {}).get(platform)
            else:
                value = data.get(key)

            if value is not None:
                entry.delete(0, tk.END)
                entry.insert(0, str(value))

    # Save 버튼 동작
    def save(self) -> None:
        data = load_config()

        # 일반 키 저장
        for key, entry in self.entries.items():
            if key.startswith("rate_"):
                continue
            data[key] = entry.get().strip()

        # CPM(rate) 저장
        rates = data.get("rates", {})
        rates["youtube"] = float(self.entries["rate_youtube"].get() or 0)
        rates["tiktok"] = float(self.entries["rate_tiktok"].get() or 0)
        rates["instagram"] = float(self.entries["rate_instagram"].get() or 0)
        data["rates"] = rates

        save_config(data)
        messagebox.showinfo("Saved", "Configuration saved.")
        get_token()  # 최초 인증 절차 실행

    # 클래스 외부에서 실행할 때 사용
def run() -> None:
    root = tk.Tk()
    SetupGUI(root)
    root.mainloop()


if __name__ == "__main__":
    run()
