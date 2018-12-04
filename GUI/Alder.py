import tkinter as tk

LARGE_FONT = ("Verdana, 12")

class Age(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Hvor gammel er du?", font="LARGE_FONT")
        label.pack(pady=10,padx=10)

        label_1 = Label(self, text="Indtast alder:", font= "LARGE_FONT")
        entry_1 = Entry(self)

        label_1.grid(row=0, sticky=E)
        entry_1.grid(row=0, column=1)

        button1 = tk.Button(self, text="Næste",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()
