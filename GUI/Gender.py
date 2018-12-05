import tkinter as tk
from tkinter import ttk
import Alder
TITLE_FONT = ("Verdana", 20, "bold")

class GenderPick(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self, master)
        label = tk.Label(self, text="Vælg køn:", font = TITLE_FONT)
        label.pack(pady=100,padx=100)

        Button_3 = ttk.Button(self, text ="Mand",
        command = lambda: master.switch_frame(Alder.Age))
        Button_3.pack(pady=100,padx=100)

        Button_4 = ttk.Button(self, text ="Kvinde",
        command = lambda: master.switch_frame(Alder.Age))
        Button_4.pack(pady=50,padx=50)
