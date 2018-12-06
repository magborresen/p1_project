import tkinter as tk
from tkinter import ttk
import Resultat
<<<<<<< HEAD
=======
import Alder
import pygame
import time
>>>>>>> 7348a06294273d98383a526c04f968bce7b4cdeb

TITLE_FONT = ("Verdana", 20, "bold")

class Test(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self, master)
        label = tk.Label(self, text="Høretest i gang...", font = TITLE_FONT)
        label.place(x=400, y=150)
        LydHort = tk.Button(self,width = 20, height = 5, text ="Hørt",
        command = lambda: master.switch_frame(Resultat.Result))

        Button_1.pack()

        # Initier pygame, som er dimsen, som afspiller lydfilerne
        pygame.mixer.init()

    #Setup til knappen

    def knaptrykket(self):


    # Funktion, som faar lydstyrken til at stige
    def increase_volume(self):
        New_volume = pygame.mixer.music.get_volume()
        pygame.mixer.music.set_volume(New_volume)
        Antal = 0
        for Antal in range (1):
            pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.01)
            time.sleep(0.01)
            Antal +=1

    def two_hundred_fifty_R(self):
        lydstyrke = 0.0
        bantal = 0
        starttid = time.time()
        for bantal in range (10):
                pygame.mixer.music.load("Frekvensafspiller/Lydfiler/250Hz_1_R.mp3")
                pygame.mixer.music.play()
                bantal +=1
            for ten_loops in range(1000):
                if knaptrykket():
                    sluttid = time.time()
                    resultattid = sluttid - starttid
                    return resultattid
                else:
                    pygame.mixer.music.set_volume(lydstyrke)
                    increase_volume()
                    lydstyrke = pygame.mixer.music.get_volume()

    def two_hundred_fifty_L(self):
        lydstyrke = 0.0
        bantal = 0
        starttid = time.time()
        for bantal in range (10):
                pygame.mixer.music.load("Frekvensafspiller/Lydfiler/250Hz_1_L.mp3")
                pygame.mixer.music.play()
                bantal +=1
            for ten_loops in range(1000):
                if knaptrykket():
                    sluttid = time.time()
                    resultattid = sluttid - starttid
                    return resultattid
                else:
                    pygame.mixer.music.set_volume(lydstyrke)
                    increase_volume()
                    lydstyrke = pygame.mixer.music.get_volume()

    def five_hundred_R(self):
        lydstyrke = 0.0
        bantal = 0
        starttid = time.time()
        for bantal in range (10):
                pygame.mixer.music.load("Frekvensafspiller/Lydfiler/500Hz_1_R.mp3")
                pygame.mixer.music.play()
                bantal +=1
            for ten_loops in range(1000):
                if knaptrykket():
                    sluttid = time.time()
                    resultattid = sluttid - starttid
                    return resultattid
                else:
                    pygame.mixer.music.set_volume(lydstyrke)
                    increase_volume()
                    lydstyrke = pygame.mixer.music.get_volume()

    def five_hundred_L(self):
        lydstyrke = 0.0
        bantal = 0
        starttid = time.time()
        for bantal in range (10):
                pygame.mixer.music.load("Frekvensafspiller/Lydfiler/500Hz_1_L.mp3")
                pygame.mixer.music.play()
                bantal +=1
            for ten_loops in range(1000):
                if knaptrykket():
                    sluttid = time.time()
                    resultattid = sluttid - starttid
                    return resultattid
                else:
                    pygame.mixer.music.set_volume(lydstyrke)
                    increase_volume()
                    lydstyrke = pygame.mixer.music.get_volume()

    def thousand_R(self):
        lydstyrke = 0.0
        bantal = 0
        starttid = time.time()
        for bantal in range (10):
                pygame.mixer.music.load("Frekvensafspiller/Lydfiler/1000Hz_1_R.mp3")
                pygame.mixer.music.play()
                bantal +=1
            for ten_loops in range(1000):
                if knaptrykket():
                    sluttid = time.time()
                    resultattid = sluttid - starttid
                    return resultattid
                else:
                    pygame.mixer.music.set_volume(lydstyrke)
                    increase_volume()
                    lydstyrke = pygame.mixer.music.get_volume()

    def thousand_L(self):
        lydstyrke = 0.0
        bantal = 0
        starttid = time.time()
        for bantal in range (10):
                pygame.mixer.music.load("Frekvensafspiller/Lydfiler/1000Hz_1_L.mp3")
                pygame.mixer.music.play()
                bantal +=1
            for ten_loops in range(1000):
                if knaptrykket():
                    sluttid = time.time()
                    resultattid = sluttid - starttid
                    return resultattid
                else:
                    pygame.mixer.music.set_volume(lydstyrke)
                    increase_volume()
                    lydstyrke = pygame.mixer.music.get_volume()

    def two_thousand_R(self):
        lydstyrke = 0.0
        bantal = 0
        starttid = time.time()
        for bantal in range (10):
                pygame.mixer.music.load("Frekvensafspiller/Lydfiler/2000Hz_1_R.mp3")
                pygame.mixer.music.play()
                bantal +=1
            for ten_loops in range(1000):
                if knaptrykket():
                    sluttid = time.time()
                    resultattid = sluttid - starttid
                    return resultattid
                else:
                    pygame.mixer.music.set_volume(lydstyrke)
                    increase_volume()
                    lydstyrke = pygame.mixer.music.get_volume()

    def two_thousand_L(self):
        lydstyrke = 0.0
        bantal = 0
        starttid = time.time()
        for bantal in range (10):
                pygame.mixer.music.load("Frekvensafspiller/Lydfiler/2000Hz_1_L.mp3")
                pygame.mixer.music.play()
                bantal +=1
            for ten_loops in range(1000):
                if knaptrykket():
                    sluttid = time.time()
                    resultattid = sluttid - starttid
                    return resultattid
                else:
                    pygame.mixer.music.set_volume(lydstyrke)
                    increase_volume()
                    lydstyrke = pygame.mixer.music.get_volume()

    def four_thousand_R(self):
        lydstyrke = 0.0
        bantal = 0
        starttid = time.time()
        for bantal in range (10):
                pygame.mixer.music.load("Frekvensafspiller/Lydfiler/4000Hz_1_R.mp3")
                pygame.mixer.music.play()
                bantal +=1
            for ten_loops in range(1000):
                if knaptrykket():
                    sluttid = time.time()
                    resultattid = sluttid - starttid
                    return resultattid
                else:
                    pygame.mixer.music.set_volume(lydstyrke)
                    increase_volume()
                    lydstyrke = pygame.mixer.music.get_volume()

    def four_thousand_L(self):
        lydstyrke = 0.0
        bantal = 0
        starttid = time.time()
        for bantal in range (10):
                pygame.mixer.music.load("Frekvensafspiller/Lydfiler/4000Hz_1_L.mp3")
                pygame.mixer.music.play()
                bantal +=1
            for ten_loops in range(1000):
                if knaptrykket():
                    sluttid = time.time()
                    resultattid = sluttid - starttid
                    return resultattid
                else:
                    pygame.mixer.music.set_volume(lydstyrke)
                    increase_volume()
                    lydstyrke = pygame.mixer.music.get_volume()

    def eight_thousand_R(self):
        lydstyrke = 0.0
        bantal = 0
        starttid = time.time()
        for bantal in range (10):
                pygame.mixer.music.load("Frekvensafspiller/Lydfiler/8000Hz_1_R.mp3")
                pygame.mixer.music.play()
                bantal +=1
            for ten_loops in range(1000):
                if knaptrykket():
                    sluttid = time.time()
                    resultattid = sluttid - starttid
                    return resultattid
                else:
                    pygame.mixer.music.set_volume(lydstyrke)
                    increase_volume()
                    lydstyrke = pygame.mixer.music.get_volume()

    def eight_thousand_L(self):
        lydstyrke = 0.0
        bantal = 0
        starttid = time.time()
        for bantal in range (10):
                pygame.mixer.music.load("Frekvensafspiller/Lydfiler/8000Hz_1_L.mp3")
                pygame.mixer.music.play()
                bantal +=1
            for ten_loops in range(1000):
                if knaptrykket():
                    sluttid = time.time()
                    resultattid = sluttid - starttid
                    return resultattid
                else:
                    pygame.mixer.music.set_volume(lydstyrke)
                    increase_volume()
                    lydstyrke = pygame.mixer.music.get_volume()

