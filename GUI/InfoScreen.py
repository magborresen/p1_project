import tkinter as tk
from tkinter import ttk
import TEST

TITLE_FONT = ("Verdana", 20, "bold")

class Information(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self, master)
        label = tk.Label(self, text="[SKRIV TEKST OM TEST HER!]:", font = TITLE_FONT)
        label.pack(pady=10,padx=10)

        Button_6 = ttk.Button(self, text ="Start test",
        command = lambda: master.switch_frame(Test.Test))
        Button_6.pack()
