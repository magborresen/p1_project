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
        LydHort = tk.Button(self,width = 20, height = 5, text ="Hørt",
        command = lambda: master.switch_frame(Resultat.Result))
        LydHort.pack()
        #Button_1.config(width = 20, height = 5)
