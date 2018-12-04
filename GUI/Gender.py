import tkinter as tk
from tkinter import ttk


TITLE_FONT = ("Verdana", 20, "bold")

class GenderPick(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self, master)
        label = tk.Label(self, text="vaelg køn:", font = TITLE_FONT)
        label.pack(pady=10,padx=10)

        Button_2 = ttk.Button(self, text ="Tilbage",
        command = lambda: master.switch_frame(MainGUI.StartPage))
        Button_2.pack()

        Button_3 = ttk.Button(self, text ="Mand",
        command = lambda: master.switch_frame(MainGUI.StartPage))
        Button_3.pack()

        Button_4 = ttk.Button(self, text ="Kvinde",
        command = lambda: master.switch_frame(MainGUI.StartPage))
        Button_4.pack()
