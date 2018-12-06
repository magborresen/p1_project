import tkinter as tk
from tkinter import ttk
import Resultat
import Alder

TITLE_FONT = ("Verdana", 20, "bold")

class Test(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self, master)
        label = tk.Label(self, text="Høretest i gang...", font = TITLE_FONT)
        label.place(x=400, y=150)
        LydHort = tk.Button(self,width = 20, height = 5, text ="Hørt",
        command = lambda: master.switch_frame(Resultat.Result))
        LydHort.place(x=400, y=240)
        #Button_1.config(width = 20, height = 5)
