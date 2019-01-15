import tkinter as tk
from tkinter import ttk
import pygame
import math


TITLE_FONT = ("Verdana", 20, "bold")

class Window(tk.Tk): # definere en class som inharits fra tk.TK

    def __init__(self, *args, **kwargs): #Method som altid køre når class er i brug
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self) #definere en container
        container.pack() #indsætter container
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self._frame = None
        self.switch_frame(Test)

    def switch_frame(self, frame_class):
        #  Destroys the old frame and packs new frame  #
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack(fill="both", expand=True)

class Test(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        label = tk.Label(self, text="db test", font=TITLE_FONT)
        label.place(x=300, y=150)
        self.sound_heard_btn = tk.Button(self, width=20, height=5, text="knap",
                                    command=lambda: self.hort())

        self.sound_heard_btn.place(x=300, y=240)

        # Initier pygame, som er dimsen, som afspiller lydfilerne
        pygame.mixer.init()

        self.test_num = 1
        self.frequency = 500
        self.ear = 0
        self.decibel = 0
        self._job = None
        volume = pygame.mixer.music.set_volume(0)

    def hort(self):
        self.sound_heard_btn["text"] = "tryk"

        print (self.decibel)
        if 1 <= self.test_num and self.frequency <= 8000:
            self.cancel_increase()
            volume = pygame.mixer.music.get_volume()
            #self.convert_to_db(volume)
            #print(self.decibel)

        if self.test_num == 1:
            self.ear = 0
            self.play_right_ear()
        elif self.test_num == 2:
            self.ear = 1
            self.play_left_ear()
        elif self.test_num == 3:
            self.ear = 0
            self.play_right_ear()
        elif self.test_num == 4:
            self.ear = 1
            self.play_left_ear()
        elif self.test_num == 5:
            self.ear = 0
            self.play_right_ear()
        elif self.test_num == 6:
            self.ear = 1
            self.play_left_ear()
        elif self.test_num == 7:
            self.ear = 0
            self.play_right_ear()
        elif self.test_num == 8:
            self.ear = 1
            self.play_left_ear()
        elif self.test_num == 9:
            self.ear = 0
            self.play_right_ear()
        elif self.test_num == 10:
            self.ear = 1
            self.play_left_ear()
        elif self.test_num == 11:
            self.ear = 0
            self.play_right_ear()
        elif self.test_num == 12:
            self.ear = 1
            self.play_left_ear()
        elif self.test_num == 13:
            pygame.mixer.music.stop()

    # Funktion, som faar lydstyrken til at stige
    def increase_volume(self):
        volume = pygame.mixer.music.get_volume()
        print (volume)
        print (self.ear)

        if volume < 0.99:
            new_volume = volume + 0.10
            pygame.mixer.music.set_volume(new_volume)
            self.convert_to_db(new_volume)
            print(self.decibel)

        else:
            self.test_num += 1
            volume = pygame.mixer.music.set_volume(0)


    # Denne funktion vil slette den tk.after() funktion der bliver kaldt i increase_volume()
    def cancel_increase(self):
        if self._job is not None:
            self.after_cancel(self._job)
            self._job = None

    # Afspiller en lydfil vha. pygame i 10 loops i det højre øre
    def play_right_ear(self):

        pygame.mixer.music.load("../Frekvensafspiller/justerede_lydfiler/" + str(self.frequency) + "Hz_R.mp3")
        pygame.mixer.music.play(1)
        self.increase_volume()

    # Afspiller en lydfil vha. pygame i 10 loops i det venstre
    def play_left_ear(self):
        pygame.mixer.music.load("../Frekvensafspiller/justerede_lydfiler/" + str(self.frequency) + "Hz_L.mp3")

        pygame.mixer.music.play(1)

        self.increase_volume()

    def convert_to_db(self, new_volume):
        self.decibel = 6.9503 * math.log(new_volume) + 40.533


app = Window()
app.geometry("800x400")
app.title("Høretester")
#app.wm_attributes('-fullscreen','true')
app.mainloop()#Holder det definerede vindue åben.
