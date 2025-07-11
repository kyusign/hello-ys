import tkinter as tk
from tkinter import messagebox

from .auth import get_token
from .config import load_config, save_config


class SetupGUI:
    def __init__(self, master: tk.Tk):
        self.master = master
        master.title('SNS Dashboard Setup')

        self.entries = {}
        fields = [
            ('YouTube Channel URL', 'youtube_url'),
            ('TikTok Channel URL', 'tiktok_url'),
            ('Instagram Channel URL', 'instagram_url'),
        ]

        for i, (label_text, key) in enumerate(fields):
            tk.Label(master, text=label_text).grid(row=i, column=0, sticky='e', pady=2, padx=2)
            entry = tk.Entry(master, width=40)
            entry.grid(row=i, column=1, pady=2, padx=2)
            self.entries[key] = entry

        tk.Button(master, text='Save', command=self.save).grid(row=len(fields), column=0, columnspan=2, pady=10)

        self.load_existing()

    def load_existing(self):
        data = load_config()
        for key, entry in self.entries.items():
            value = data.get(key)
            if value is not None:
                entry.delete(0, tk.END)
                entry.insert(0, str(value))

    def save(self):
        data = load_config()
        for key, entry in self.entries.items():
            data[key] = entry.get().strip()
        save_config(data)
        messagebox.showinfo('Saved', 'Configuration saved.')
        get_token()


def run():
    root = tk.Tk()
    SetupGUI(root)
    root.mainloop()


if __name__ == '__main__':
    run()
