import tkinter as tk
from tkinter import ttk
import InfoScreen
import json

TITLE_FONT = ("Verdana", 20, "bold")


class Age(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        label = tk.Label(self, text="Hvor gammel er du?", font=TITLE_FONT)
        label.place(x=380, y=150)

        label_1 = tk.Label(self, text="Indtast alder:", font="TITLE_FONT")
        self.age_entry = tk.Entry(self)

        label_1.place(x=450, y=200)
        self.age_entry.place(x=400, y=220)

        if self.age_entry.get() == "":
            print (self.age_entry.get())

        TilInfo = tk.Button(self, text="Næste", width = 20, height = 5,
                            command=lambda: [self.update_json(),
                                             master.switch_frame(InfoScreen.Information)])
        TilInfo.place(x=400, y=280)

    def update_json(self):
        age_answer = self.age_entry.get()
        with open('../variables.json', 'r+') as f:
            data = json.load(f)
            data["Age"] = int(age_answer)
            f.seek(0)
            json.dump(data, f)
            f.truncate()
