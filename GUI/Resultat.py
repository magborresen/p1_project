import tkinter as tk
from tkinter import ttk
import MainGUI

TITLE_FONT = ("Verdana", 20, "bold")

class Result(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self, master)
        label = tk.Label(self, text="[SKRIV TEKST OM RESULTATET HER!]:", font = TITLE_FONT)
        label.pack(pady=10,padx=10)

        Button_6 = ttk.Button(self, text ="Ny test",
        command = lambda: master.switch_frame(MainGUI.StartPage))
        Button_6.pack()
