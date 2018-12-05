# Importer de nodvendige biblioteker
import pygame
import time

# Initier pygame, som er dimsen, som afspiller lydfilerne
pygame.mixer.init()
# Angiv start volumen



def increase_volume():
    New_volume = pygame.mixer.music.get_volume()
    pygame.mixer.music.set_volume(New_volume)
    Antal = 0
    for Antal in range (10):
        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.01)
        time.sleep(1)
        Antal +=1

def two_hundred_fifty():
    lydstyrke = 0.0
    starttid = time.time()
    for ten_loops in range(10):
        if knaptrykket():
            sluttid = time.time()
            resultattid = sluttid - starttid
            return resultattid
        else:
            pygame.mixer.music.load("Frekvensafspiller/Lydfiler/250Hz_1.mp3")
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(lydstyrke)
            increase_volume()
            lydstyrke = pygame.mixer.music.get_volume()


def five_hundred():
    lydstyrke = 0.0
    starttid = time.time()
    for ten_loops in range(10):
        if knaptrykket():
            sluttid = time.time()
            resultattid = sluttid - starttid
            return resultattid
        else:
            pygame.mixer.music.load("Frekvensafspiller/Lydfiler/500Hz_1.mp3")
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(lydstyrke)
            increase_volume()
            lydstyrke = pygame.mixer.music.get_volume()

def thousand():
    lydstyrke = 0.0
    starttid = time.time()
    for ten_loops in range(10):
        if knaptrykket():
            sluttid = time.time()
            resultattid = sluttid - starttid
            return resultattid
        else:
            pygame.mixer.music.load("Frekvensafspiller/Lydfiler/1000Hz_1.mp3")
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(lydstyrke)
            increase_volume()
            lydstyrke = pygame.mixer.music.get_volume()

def two_thousand():
    lydstyrke = 0.0
    starttid = time.time()
    for ten_loops in range(10):
        if knaptrykket():
            sluttid = time.time()
            resultattid = sluttid - starttid
            return resultattid
        else:
            pygame.mixer.music.load("Frekvensafspiller/Lydfiler/2000Hz_1.mp3")
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(lydstyrke)
            increase_volume()
            lydstyrke = pygame.mixer.music.get_volume()

def four_thousand():
    lydstyrke = 0.0
    starttid = time.time()
    for ten_loops in range(10):
        if knaptrykket():
            sluttid = time.time()
            resultattid = sluttid - starttid
            return resultattid
        else:
            pygame.mixer.music.load("Frekvensafspiller/Lydfiler/4000Hz_1.mp3")
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(lydstyrke)
            increase_volume()
            lydstyrke = pygame.mixer.music.get_volume()

def eight_thousand():
    lydstyrke = 0.0
    starttid = time.time()
    for ten_loops in range(10):
        if knaptrykket():
            sluttid = time.time()
            resultattid = sluttid - starttid
            return resultattid
        else:
            pygame.mixer.music.load("Frekvensafspiller/Lydfiler/8000Hz_1.mp3")
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(lydstyrke)
            increase_volume()
            lydstyrke = pygame.mixer.music.get_volume()



resultattid_two_hundred_fifty = two_hundred_fifty()
resultattid_five_hundred = five_hundred()
resultattid_thousand = thousand()
resultattid_two_thousand = two_thousand()
resultattid_four_thousand = four_thousand()
resultattid_eight_thousand = eight_thousand()
