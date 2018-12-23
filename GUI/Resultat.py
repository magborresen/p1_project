import tkinter as tk
from tkinter import ttk
import MainGUI

TITLE_FONT = ("Verdana", 20, "bold")

class Result(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self, master)
        label = tk.Label(self, text="Resultat:", font = TITLE_FONT)
        label.place(x=300, y=100)

        New_Test = tk.Button(self, width = 20, height = 5, text ="Ny test",
        command = lambda: master.switch_frame(MainGUI.StartPage))
        New_Test.place(x=300, y=270)
