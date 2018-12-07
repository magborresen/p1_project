import tkinter as tk
from tkinter import ttk
import Resultat
import Alder
import pygame
import time

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

        self.test_tal = 0

    def hort(self):
        self.test_tal += 1
        if self.test_tal > 1:
            volume = pygame.mixer.music.get_volume()
            print (volume)

        if self.test_tal == 1:
            self.two_hundred_fifty_R()
        elif self.test_tal == 2:
            self.two_hundred_fifty_L()
        elif self.test_tal == 3:
            self.five_hundred_R()
        elif self.test_tal == 4:
            self.five_hundred_L()
        elif self.test_tal == 5:
            self.thousand_R()
        elif self.test_tal == 6:
            self.thousand_L()
        elif self.test_tal == 7:
            self.two_thousand_R()
        elif self.test_tal == 8:
            self.two_thousand_L()
        elif self.test_tal == 9:
            self.four_thousand_R()
        elif self.test_tal == 10:
            self.four_thousand_L()
        elif self.test_tal == 11:
            self.eight_thousand_R()
        elif self.test_tal == 12:
            self.eight_thousand_L()


    # Funktion, som faar lydstyrken til at stige
    def increase_volume(self):
        New_volume = pygame.mixer.music.get_volume()
        pygame.mixer.music.set_volume(New_volume)
        Antal = 0
        for Antal in range(1):
            pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.01)
            time.sleep(0.01)
            Antal += 1

    def two_hundred_fifty_R(self):
        lydstyrke = 0.0
        bantal = 0
        for bantal in range(10):
            pygame.mixer.music.load("../Frekvensafspiller/Lydfiler/250Hz_1_R.mp3")
            pygame.mixer.music.play()
            bantal += 1
            for ten_loops in range(1000):
                pygame.mixer.music.set_volume(lydstyrke)
                self.increase_volume()
                lydstyrke = pygame.mixer.music.get_volume()

    def two_hundred_fifty_L(self):
        lydstyrke = 0.0
        bantal = 0
        for bantal in range(10):
            pygame.mixer.music.load("../Frekvensafspiller/Lydfiler/250Hz_1_L.mp3")
            pygame.mixer.music.play()
            bantal += 1
            for ten_loops in range(1000):
                pygame.mixer.music.set_volume(lydstyrke)
                self.increase_volume()
                lydstyrke = pygame.mixer.music.get_volume()

    def five_hundred_R(self):
        lydstyrke = 0.0
        bantal = 0
        for bantal in range(10):
            pygame.mixer.music.load("../Frekvensafspiller/Lydfiler/500Hz_1_R.mp3")
            pygame.mixer.music.play()
            bantal += 1
            for ten_loops in range(1000):
                pygame.mixer.music.set_volume(lydstyrke)
                self.increase_volume()
                lydstyrke = pygame.mixer.music.get_volume()

    def five_hundred_L(self):
        lydstyrke = 0.0
        bantal = 0
        for bantal in range(10):
            pygame.mixer.music.load("../Frekvensafspiller/Lydfiler/500Hz_1_L.mp3")
            pygame.mixer.music.play()
            bantal += 1
            for ten_loops in range(1000):
                pygame.mixer.music.set_volume(lydstyrke)
                self.increase_volume()
                lydstyrke = pygame.mixer.music.get_volume()

    def thousand_R(self):
        lydstyrke = 0.0
        bantal = 0
        for bantal in range(10):
            pygame.mixer.music.load("../Frekvensafspiller/Lydfiler/1000Hz_1_R.mp3")
            pygame.mixer.music.play()
            bantal += 1
            for ten_loops in range(1000):
                pygame.mixer.music.set_volume(lydstyrke)
                self.increase_volume()
                lydstyrke = pygame.mixer.music.get_volume()

    def thousand_L(self):
        lydstyrke = 0.0
        bantal = 0
        for bantal in range(10):
            pygame.mixer.music.load("../Frekvensafspiller/Lydfiler/1000Hz_1_L.mp3")
            pygame.mixer.music.play()
            bantal += 1
            for ten_loops in range(1000):
                pygame.mixer.music.set_volume(lydstyrke)
                self.increase_volume()
                lydstyrke = pygame.mixer.music.get_volume()

    def two_thousand_R(self):
        lydstyrke = 0.0
        bantal = 0
        for bantal in range(10):
            pygame.mixer.music.load("../Frekvensafspiller/Lydfiler/2000Hz_1_R.mp3")
            pygame.mixer.music.play()
            bantal += 1
            for ten_loops in range(1000):
                pygame.mixer.music.set_volume(lydstyrke)
                self.increase_volume()
                lydstyrke = pygame.mixer.music.get_volume()

    def two_thousand_L(self):
        lydstyrke = 0.0
        bantal = 0
        for bantal in range(10):
            pygame.mixer.music.load("../Frekvensafspiller/Lydfiler/2000Hz_1_L.mp3")
            pygame.mixer.music.play()
            bantal += 1
            for ten_loops in range(1000):
                    pygame.mixer.music.set_volume(lydstyrke)
                    self.increase_volume()
                    lydstyrke = pygame.mixer.music.get_volume()

    def four_thousand_R(self):
        lydstyrke = 0.0
        bantal = 0
        for bantal in range(10):
            pygame.mixer.music.load("../Frekvensafspiller/Lydfiler/4000Hz_1_R.mp3")
            pygame.mixer.music.play()
            bantal += 1
            for ten_loops in range(1000):
                pygame.mixer.music.set_volume(lydstyrke)
                self.increase_volume()
                lydstyrke = pygame.mixer.music.get_volume()

    def four_thousand_L(self):
        lydstyrke = 0.0
        bantal = 0
        for bantal in range(10):
            pygame.mixer.music.load("../Frekvensafspiller/Lydfiler/4000Hz_1_L.mp3")
            pygame.mixer.music.play()
            bantal += 1
            for ten_loops in range(1000):
                pygame.mixer.music.set_volume(lydstyrke)
                self.increase_volume()
                lydstyrke = pygame.mixer.music.get_volume()

    def eight_thousand_R(self):
        lydstyrke = 0.0
        bantal = 0
        for bantal in range(10):
            pygame.mixer.music.load("../Frekvensafspiller/Lydfiler/8000Hz_1_R.mp3")
            pygame.mixer.music.play()
            bantal += 1
            for ten_loops in range(1000):
                pygame.mixer.music.set_volume(lydstyrke)
                self.increase_volume()
                lydstyrke = pygame.mixer.music.get_volume()

    def eight_thousand_L(self):
        lydstyrke = 0.0
        bantal = 0
        for bantal in range(10):
            pygame.mixer.music.load("../Frekvensafspiller/Lydfiler/8000Hz_1_L.mp3")
            pygame.mixer.music.play()
            bantal += 1
            for ten_loops in range(1000):
                pygame.mixer.music.set_volume(lydstyrke)
                self.increase_volume()
                lydstyrke = pygame.mixer.music.get_volume()
