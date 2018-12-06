import tkinter as tk
from tkinter import ttk
import Alder
import json
TITLE_FONT = ("Verdana", 20, "bold")


class GenderPick(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        label = tk.Label(self, text="Vælg køn:", font=TITLE_FONT)
        label.pack(pady=100, padx=100)

        Button_3 = ttk.Button(self, text="Mand",
                              command=lambda: [self.update_json_man(),
                                               master.switch_frame(Alder.Age)])
        Button_3.pack(pady=100, padx=100)

        Button_4 = ttk.Button(self, text="Kvinde",
                              command=lambda: [self.update_json_woman(self),
                                               master.switch_frame(Alder.Age)])
        Button_4.pack(pady=50, padx=50)

    def update_json_woman(self):
        with open('../variables.json', 'r+') as f:
            data = json.load(f)
            data['Gender'] = "Kvinde"
            f.seek(0)
            json.dump(data, f)
            f.truncate()

    def update_json_man(self):
        with open('../variables.json', 'r+') as f:
            data = json.load(f)
            data["Gender"] = "Mand"
            f.seek(0)
            json.dump(data, f)
            f.truncate()
