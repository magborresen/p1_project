import tkinter as tk
from tkinter import ttk
import Resultat
import pygame
import alsaaudio
from datetime import datetime
import json
import math
import sys
sys.path.append("../Result/")
import calculate_result
TITLE_FONT = ("Verdana", 20, "bold")


class Test(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        label = tk.Label(self, text="Høretest i gang...", font=TITLE_FONT)
        label.place(x=300, y=150)
        self.sound_heard_btn = tk.Button(self, width=20, 
                                         height=5,
                                         text="Start Test",
                                         command=lambda: self.hort())

        self.sound_heard_btn.place(x=300, y=240)

        # Initier pygame, som er dimsen, som afspiller lydfilerne
        pygame.mixer.init()
        self.m = alsaaudio.Mixer('PCM')

        self.test_num = 0
        self.frequency = 250
        self.ear = 0
        self.decibel = 0
        self._job = None

    def hort(self):
        self.sound_heard_btn["text"] = "Hørt"
        self.test_num += 1
        print(self.frequency)
        if self.test_num > 1 and self.decibel <= 8000:
            self.cancel_increase()
            volume = self.m.getvolume()
            self.convert_to_db(self.frequency, volume)
            self.update_json(self.ear, self.decibel)
            print(volume)

        if self.test_num % 2 != 0 and self.test_num <= 12:
            self.ear = 0
            self.play_right_ear()
        elif self.test_num % 2 == 0 and self.test_num <= 12:
            self.ear = 1
            self.play_left_ear()

        elif self.test_num == 13:
            pygame.mixer.music.stop()
            calculate_result.calc_mean()
            self.master.switch_frame(Resultat.Result)

    # Funktion, som faar lydstyrken til at stige
    def increase_volume(self):
        volume = self.m.getvolume()
        print(volume)
        print(datetime.now().time())
        if volume < 1.0:
            new_volume = volume + 1
            self.m.setvolume(new_volume)
            self._job = self.after(1000, self.increase_volume)

    # Denne funktion vil slette den tk.after() funktion der bliver kaldt i increase_volume()
    def cancel_increase(self):
        if self._job is not None:
            self.after_cancel(self._job)
            self._job = None

    # Afspiller en lydfil vha. pygame i 10 loops i det højre øre
    def play_right_ear(self):
        volume = 0
        pygame.mixer.music.load("../Frekvensafspiller/justerede_lydfiler/" + str(self.frequency) + "Hz_R.mp3")

        self.m.setvolume(volume)
        pygame.mixer.music.play(10)
        self.increase_volume()

    # Afspiller en lydfil vha. pygame i 10 loops i det venstre
    def play_left_ear(self):
        volume = 0
        pygame.mixer.music.load("../Frekvensafspiller/justerede_lydfiler/" + str(self.frequency) + "Hz_L.mp3")

        self.m.setvolume(volume)
        pygame.mixer.music.play(10)

        if self.frequency <= 8000:
            self.frequency = self.frequency * 2

        self.increase_volume()

    # Omregner volumen til decibel ud fra funktion fra tendenslinje
    def convert_to_db(self, frequency, volume):
        self.decibel = 6.9503 * math.log(volume) + 40.533

        conversions = {'250': 24.676*math.log(volume)-39.069,
                       '500': 23.192*math.log(volume)-22.864,
                       '1000': 22.921*math.log(volume)-11.822,
                       '2000': 23.303*math.log(volume)-10.235,
                       '4000': 25.698*math.log(volume)-15.704,
                       '8000': 25.709*math.log(volume)-21.697}

        for k, v in conversions.items():
            if k == frequency:
                self.decibel = v

    def update_json(self, ear, decibel):
        '''Funktionen åbner variables.json og gennem den
        omregnede decibel i den passsende frekvens
        på det passende øre'''
        if ear == 0:
            with open('../variables.json', 'r+') as f:
                data = json.load(f)
                data["right_ear_test"][str(self.frequency)] = decibel
                f.seek(0)
                json.dump(data, f)
                f.truncate()
        elif ear == 1:
            with open('../variables.json', 'r+') as f:
                data = json.load(f)
                data["left_ear_test"][str(self.frequency)] = decibel
                f.seek(0)
                json.dump(data, f)
                f.truncate()