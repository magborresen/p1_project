import tkinter as tk
from tkinter import ttk
import Resultat
import Alder

TITLE_FONT = ("Verdana", 20, "bold")

class Test(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self, master)
        label = tk.Label(self, text="Høretest i gang...", font = TITLE_FONT)
        label.pack(pady=10,padx=10)
        print(Alder.__init__.age_entry)
        Button_1 = ttk.Button(self, text ="Hørt",
        command = lambda: master.switch_frame(Resultat.Result))
        Button_1.pack()
