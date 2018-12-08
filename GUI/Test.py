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
        label.place(x=400, y=150)
        sound_heard_btn = tk.Button(self, width=20, height=5, text="Hørt",
                                    command=lambda: self.hort())

        sound_heard_btn.pack()

        # Initier pygame, som er dimsen, som afspiller lydfilerne
        pygame.mixer.init()

        self.test_num = 0

    def hort(self):
        self.test_num += 1
        if self.test_num > 1:
            volume = pygame.mixer.music.get_volume()
            print (volume)

        if self.test_num == 1:
            self.two_hundred_fifty_R()
        elif self.test_num == 2:
            self.two_hundred_fifty_L()
        elif self.test_num == 3:
            self.five_hundred_R()
        elif self.test_num == 4:
            self.five_hundred_L()
        elif self.test_num == 5:
            self.thousand_R()
        elif self.test_num == 6:
            self.thousand_L()
        elif self.test_num == 7:
            self.two_thousand_R()
        elif self.test_num == 8:
            self.two_thousand_L()
        elif self.test_num == 9:
            self.four_thousand_R()
        elif self.test_num == 10:
            self.four_thousand_L()
        elif self.test_num == 11:
            self.eight_thousand_R()
        elif self.test_num == 12:
            self.eight_thousand_L()

    # Funktion, som faar lydstyrken til at stige
    def increase_volume(self):
        New_volume = pygame.mixer.music.get_volume()
        pygame.mixer.music.set_volume(New_volume)
        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.01)
        self.master.after(50, self.increase_volume())

    def two_hundred_fifty_R(self):
        lydstyrke = 0.0
        pygame.mixer.music.load("../Frekvensafspiller/Lydfiler/250Hz_1_R.mp3")
        pygame.mixer.music.play(10)
        while True:
        #for ten_loops in range(1000):
        pygame.mixer.music.set_volume(lydstyrke)
        self.increase_volume()
        lydstyrke = pygame.mixer.music.get_volume()

    def two_hundred_fifty_L(self):
        lydstyrke = 0.0
        pygame.mixer.music.load("../Frekvensafspiller/Lydfiler/250Hz_1_L.mp3")
        pygame.mixer.music.play(10)
        for ten_loops in range(1000):
            pygame.mixer.music.set_volume(lydstyrke)
            self.increase_volume()
            lydstyrke = pygame.mixer.music.get_volume()

    def five_hundred_R(self):
        lydstyrke = 0.0
        pygame.mixer.music.load("../Frekvensafspiller/Lydfiler/500Hz_1_R.mp3")
        pygame.mixer.music.play(10)
        for ten_loops in range(1000):
            pygame.mixer.music.set_volume(lydstyrke)
            self.increase_volume()
            lydstyrke = pygame.mixer.music.get_volume()

    def five_hundred_L(self):
        lydstyrke = 0.0
        pygame.mixer.music.load("../Frekvensafspiller/Lydfiler/500Hz_1_L.mp3")
        pygame.mixer.music.play(10)
        for ten_loops in range(1000):
            pygame.mixer.music.set_volume(lydstyrke)
            self.increase_volume()
            lydstyrke = pygame.mixer.music.get_volume()

    def thousand_R(self):
        lydstyrke = 0.0
        pygame.mixer.music.load("../Frekvensafspiller/Lydfiler/1000Hz_1_R.mp3")
        pygame.mixer.music.play(10)
        for ten_loops in range(1000):
            pygame.mixer.music.set_volume(lydstyrke)
            self.increase_volume()
            lydstyrke = pygame.mixer.music.get_volume()

    def thousand_L(self):
        lydstyrke = 0.0
        pygame.mixer.music.load("../Frekvensafspiller/Lydfiler/1000Hz_1_L.mp3")
        pygame.mixer.music.play(10)
        for ten_loops in range(1000):
            pygame.mixer.music.set_volume(lydstyrke)
            self.increase_volume()
            lydstyrke = pygame.mixer.music.get_volume()

    def two_thousand_R(self):
        lydstyrke = 0.0
        pygame.mixer.music.load("../Frekvensafspiller/Lydfiler/2000Hz_1_R.mp3")
        pygame.mixer.music.play(10)
        for ten_loops in range(1000):
            pygame.mixer.music.set_volume(lydstyrke)
            self.increase_volume()
            lydstyrke = pygame.mixer.music.get_volume()

    def two_thousand_L(self):
        lydstyrke = 0.0
        pygame.mixer.music.load("../Frekvensafspiller/Lydfiler/2000Hz_1_L.mp3")
        pygame.mixer.music.play(10)
        for ten_loops in range(1000):
                pygame.mixer.music.set_volume(lydstyrke)
                self.increase_volume()
                lydstyrke = pygame.mixer.music.get_volume()

    def four_thousand_R(self):
        lydstyrke = 0.0
        pygame.mixer.music.load("../Frekvensafspiller/Lydfiler/4000Hz_1_R.mp3")
        pygame.mixer.music.play(10)
        for ten_loops in range(1000):
            pygame.mixer.music.set_volume(lydstyrke)
            self.increase_volume()
            lydstyrke = pygame.mixer.music.get_volume()

    def four_thousand_L(self):
        lydstyrke = 0.0
        pygame.mixer.music.load("../Frekvensafspiller/Lydfiler/4000Hz_1_L.mp3")
        pygame.mixer.music.play(10)
        for ten_loops in range(1000):
            pygame.mixer.music.set_volume(lydstyrke)
            self.increase_volume()
            lydstyrke = pygame.mixer.music.get_volume()

    def eight_thousand_R(self):
        lydstyrke = 0.0
        pygame.mixer.music.load("../Frekvensafspiller/Lydfiler/8000Hz_1_R.mp3")
        pygame.mixer.music.play(10)
        for ten_loops in range(1000):
            pygame.mixer.music.set_volume(lydstyrke)
            self.increase_volume()
            lydstyrke = pygame.mixer.music.get_volume()

    def eight_thousand_L(self):
        lydstyrke = 0.0
        pygame.mixer.music.load("../Frekvensafspiller/Lydfiler/8000Hz_1_L.mp3")
        pygame.mixer.music.play(10)
        for ten_loops in range(1000):
            pygame.mixer.music.set_volume(lydstyrke)
            self.increase_volume()
            lydstyrke = pygame.mixer.music.get_volume()
