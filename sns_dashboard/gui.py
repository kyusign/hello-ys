import json
import os
import tkinter as tk
from tkinter import messagebox

from .auth import get_token

CONFIG_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config.json')


class SetupGUI:
    def __init__(self, master: tk.Tk):
        self.master = master
        master.title('SNS Dashboard Setup')

        self.entries = {}
        fields = [
            ('Google Client ID', 'google_client_id'),
            ('Google Client Secret', 'google_client_secret'),
            ('Instagram Client ID', 'instagram_client_id'),
            ('Instagram Client Secret', 'instagram_client_secret'),
            ('TikTok Client Key', 'tiktok_client_key'),
            ('TikTok Client Secret', 'tiktok_client_secret'),
            ('Spreadsheet ID', 'spreadsheet_id'),
        ]

        for i, (label_text, key) in enumerate(fields):
            tk.Label(master, text=label_text).grid(row=i, column=0, sticky='e', pady=2, padx=2)
            entry = tk.Entry(master, width=40)
            entry.grid(row=i, column=1, pady=2, padx=2)
            self.entries[key] = entry

        tk.Button(master, text='Save', command=self.save).grid(row=len(fields), column=0, columnspan=2, pady=10)

        self.load_existing()

    def load_existing(self):
        if not os.path.exists(CONFIG_FILE):
            return
        with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for key, entry in self.entries.items():
            if key in data:
                entry.delete(0, tk.END)
                entry.insert(0, data[key])

    def save(self):
        data = {key: entry.get().strip() for key, entry in self.entries.items()}
        with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
        messagebox.showinfo('Saved', 'Configuration saved.')
        get_token()

def run():
    root = tk.Tk()
    SetupGUI(root)
    root.mainloop()


if __name__ == '__main__':
    run()
