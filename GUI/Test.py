import tkinter as tk
from tkinter import ttk
import Resultat
import Alder
import pygame
import time
import json
TITLE_FONT = ("Verdana", 20, "bold")


class Test(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        label = tk.Label(self, text="Høretest i gang...", font=TITLE_FONT)
        label.place(x=300, y=150)
        sound_heard_btn = tk.Button(self, width=20, height=5, text="Hørt",
                                    command=lambda: self.hort())

        sound_heard_btn.place(x=300, y=240)

        # Initier pygame, som er dimsen, som afspiller lydfilerne
        pygame.mixer.init()

        self.test_num = 0
        self.frequency = 250
        self.ear = 0

    def hort(self):
        self.test_num += 1
        print (self.frequency)
        if self.test_num > 1:
            volume = pygame.mixer.music.get_volume()
            self.update_json(self.ear, volume)
            print (volume)

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
            self.master.switch_frame(Resultat.Result)

    # Funktion, som faar lydstyrken til at stige
    def increase_volume(self):
        volume = pygame.mixer.music.get_volume()
        print (volume)
        if volume < 1.0:
            new_volume = volume + 0.01
            pygame.mixer.music.set_volume(new_volume)
            self.after(1000, self.increase_volume)

    def play_right_ear(self):
        volume = 0.000
        pygame.mixer.music.load("../Frekvensafspiller/Lydfiler/" + str(self.frequency) + "Hz_1_R.mp3")
        pygame.mixer.music.play(10)

        pygame.mixer.music.set_volume(volume)
        self.increase_volume()

    def play_left_ear(self):
        volume = 0.000
        pygame.mixer.music.load("../Frekvensafspiller/Lydfiler/" + str(self.frequency) + "Hz_1_L.mp3")
        pygame.mixer.music.play(10)

        pygame.mixer.music.set_volume(volume)
        self.frequency = self.frequency * 2
        self.increase_volume()

    def update_json(self, ear, volume):
        if ear == 0:
            with open('../variables.json', 'r+') as f:
                data = json.load(f)
                data["right_ear_test"][str(self.frequency)] = volume
                f.seek(0)
                json.dump(data, f)
                f.truncate()
        elif ear == 1:
            with open('../variables.json', 'r+') as f:
                data = json.load(f)
                data["left_ear_test"][str(self.frequency)] = volume
                f.seek(0)
                json.dump(data, f)
                f.truncate()
