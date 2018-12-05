import tkinter as tk
from tkinter import ttk
import InfoScreen
import json
TITLE_FONT = ("Verdana", 20, "bold")


class Age(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        label = tk.Label(self, text="Hvor gammel er du?", font="TITLE_FONT")
        label.pack(pady=10, padx=10)

        label_1 = tk.Label(self, text="Indtast alder:", font="TITLE_FONT")
        self.age_entry = tk.Entry(self)

        label_1.pack()
        self.age_entry.pack()

        if self.age_entry.get() == "":
            print (self.age_entry.get())

        button1 = ttk.Button(self, text="Næste",
                            command=lambda: [self.update_json(),
                                             master.switch_frame(InfoScreen.Information)])
        button1.pack()

    def update_json(self):
        age_answer = self.age_entry.get()
        with open('../variables.json', 'r+') as f:
            data = json.load(f)
            data["Age"] = int(age_answer)
            f.seek(0)
            json.dump(data, f)
            f.truncate()
