import tkinter as tk
from tkinter import ttk
import Resultat
import Test
import InfoScreen
import Alder
import Gender

geom=""


TITLE_FONT = ("Verdana", 20, "bold")


class Window(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack()
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self._frame = None
        self.switch_frame(StartPage)

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
        label = tk.Label(self, text="Høretester V.1",
                         font=TITLE_FONT)
        label.pack(padx=10, pady=10)

        button1 = tk.Button(self, text="Kom Igang",
                            command=lambda: master.switch_frame(
                                Gender.GenderPick))
        button1.pack(fill="x")



app = Window()
app.wm_attributes('-fullscreen','true')
app.mainloop()
