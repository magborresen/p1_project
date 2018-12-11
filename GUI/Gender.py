import tkinter as tk
from tkinter import ttk
import Alder
import json
TITLE_FONT = ("Verdana", 20, "bold")


class GenderPick(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        label = tk.Label(self, text="Vælg køn:", font=TITLE_FONT)
        label.place(x=330, y=150)

        Next_Gender = tk.Button(self, text="Mand", width=20, height=5,
                                command=lambda: [self.update_json_man(),
                                                 master.switch_frame(Alder.Age)])
        Next_Gender.place(x=150, y=240)

        Next_Gender2 = tk.Button(self, text="Kvinde", width= 20, height=5,
                                 command=lambda: [self.update_json_woman(),
                                                  master.switch_frame(Alder.Age)])
        Next_Gender2.place(x=450, y=240)

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
