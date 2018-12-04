import tkinter as tk
TITLE_FONT = ("Verdana", 20, "bold")

class Test(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self, master)
        label = tk.Label(self, text="Høretest i gang...", font = TITLE_FONT)
        label.pack(pady=10,padx=10)

        Button_1 = tk.Button(self, text ="Hoart",
        command = lambda: master.switch_frame(MainGUI.StartPage))
        Button_1.pack()
