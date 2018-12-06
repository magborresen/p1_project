import tkinter as tk
from tkinter import ttk
import MainGUI

TITLE_FONT = ("Verdana", 20, "bold")

class Result(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self, master)
        label = tk.Label(self, text="Resultat:", font = TITLE_FONT)
        label.place(x=400, y=100)

        NyTest = tk.Button(self, width = 20, height = 5, text ="Ny test",
        command = lambda: master.switch_frame(MainGUI.StartPage))
        NyTest.place(x=400, y=320)
