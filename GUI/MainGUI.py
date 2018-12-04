import tkinter as tk

import Alder

LARGE_FONT = ("Times New Roman", 12)


class Horetester(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self) #indeholder alt vi indsaetter
        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Alder):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0,column = 0, sticky="nsew")


        self.show_frame(StartPage)


    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__ (self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start side", font = LARGE_FONT)
        label.pack(pady=10,padx=10)

        Button_1 = tk.Button(self, text ="Kom igang",
        command = lambda: controller.show_frame(Alder.Age))
        Button_1.pack()



app=Horetester()
app.mainloop()
