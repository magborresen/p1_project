import tkinter as tk
<<<<<<< HEAD

import Alder
=======
from tkinter import ttk
import Gender
>>>>>>> 760f0261477f9350117cb681e5d6513193efbf5d

TITLE_FONT = ("Verdana", 20, "bold")


class Window(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

<<<<<<< HEAD
        container = tk.Frame(self) #indeholder alt vi indsaetter
        container.pack(side="top", fill="both", expand = True)
=======
        tk.Tk.wm_title(self, "AnyGrapher")
>>>>>>> 760f0261477f9350117cb681e5d6513193efbf5d

        container = tk.Frame(self)
        container.pack()
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

<<<<<<< HEAD
        self.frames = {}

        for F in (StartPage, Alder):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0,column = 0, sticky="nsew")


        self.show_frame(StartPage)

=======
        self._frame = None
        self.switch_frame(StartPage)
>>>>>>> 760f0261477f9350117cb681e5d6513193efbf5d

    def switch_frame(self, frame_class):
        #  Destroys the old frame and packs new frame  #
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack(fill="both", expand=True)


class StartPage(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        label = tk.Label(self, text="Horetester V.1",
                         font=TITLE_FONT)
        label.pack(padx=10, pady=10)

<<<<<<< HEAD
        Button_1 = tk.Button(self, text ="Kom igang",
        command = lambda: controller.show_frame(Alder.Age))
        Button_1.pack()



app=Horetester()
=======
        button1 = tk.Button(self, text="Kom Igang",
                            command=lambda: master.switch_frame(
                                Gender.GenderPick))
        button1.pack(fill="x")



app = Window()
>>>>>>> 760f0261477f9350117cb681e5d6513193efbf5d
app.mainloop()
