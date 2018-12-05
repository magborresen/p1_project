import tkinter as tk
from tkinter import ttk
import InfoScreen

TITLE_FONT = ("Verdana", 20, "bold")


class Age(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        label = tk.Label(self, text="Hvor gammel er du?", font="TITLE_FONT")
        label.pack(pady=10,padx=10)

        label_1 = tk.Label(self, text="Indtast alder:", font= "TITLE_FONT")
<<<<<<< HEAD
        entry_1 = tk.Entry(self)
=======
        age_entry = tk.Entry(self)
>>>>>>> e4a4a1f810afc5be99019255f28f068e1b12e260

        label_1.pack()
        age_entry.pack()

        button1 = ttk.Button(self, text="Næste",
                            command=lambda: master.switch_frame(InfoScreen.Information))
        button1.pack()
