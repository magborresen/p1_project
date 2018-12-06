# Importer de nodvendige biblioteker
import pygame
import time

# Initier pygame, som er dimsen, som afspiller lydfilerne
pygame.mixer.init()

#Afspil 250Hz
def two_hundred_fifty():
    Antal = 0
    bantal = 0
    lydstyrke = 0.1
    for bantal in range (9):
        pygame.mixer.music.set_volume(lydstyrke)
        pygame.mixer.music.load("Frekvensafspiller/Lydfiler_L+R/250Hz_1.mp3")
        pygame.mixer.music.play()
        time.sleep(10)
        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.1)
        lydstyrke = pygame.mixer.music.get_volume()
        bantal +=1

#Afspil 500Hz
def five_hundred():
    Antal = 0
    bantal = 0
    lydstyrke = 0.1
    for bantal in range (9):
        pygame.mixer.music.set_volume(lydstyrke)
        pygame.mixer.music.load("Frekvensafspiller/Lydfiler_L+R/500Hz_1.mp3")
        pygame.mixer.music.play()
        time.sleep(10)
        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.1)
        lydstyrke = pygame.mixer.music.get_volume()
        bantal +=1

#Afspil 1000Hz
def thousand():
    Antal = 0
    bantal = 0
    lydstyrke = 0.1
    for bantal in range (9):
        pygame.mixer.music.set_volume(lydstyrke)
        pygame.mixer.music.load("Frekvensafspiller/Lydfiler_L+R/1000Hz_1.mp3")
        pygame.mixer.music.play()
        time.sleep(10)
        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.1)
        lydstyrke = pygame.mixer.music.get_volume()
        bantal +=1

#Afspil 2000Hz
def two_thousand():
    Antal = 0
    bantal = 0
    lydstyrke = 0.1
    for bantal in range (9):
        pygame.mixer.music.set_volume(lydstyrke)
        pygame.mixer.music.load("Frekvensafspiller/Lydfiler_L+R/2000Hz_1.mp3")
        pygame.mixer.music.play()
        time.sleep(10)
        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.1)
        lydstyrke = pygame.mixer.music.get_volume()
        bantal +=1

#Afspil 4000Hz
def four_thousand():
    Antal = 0
    bantal = 0
    lydstyrke = 0.1
    for bantal in range (9):
        pygame.mixer.music.set_volume(lydstyrke)
        pygame.mixer.music.load("Frekvensafspiller/Lydfiler_L+R/4000Hz_1.mp3")
        pygame.mixer.music.play()
        time.sleep(10)
        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.1)
        lydstyrke = pygame.mixer.music.get_volume()
        bantal +=1

#Afspil 8000Hz
def eight_thousand():
    Antal = 0
    bantal = 0
    lydstyrke = 0.1
    for bantal in range (9):
        pygame.mixer.music.set_volume(lydstyrke)
        pygame.mixer.music.load("Frekvensafspiller/Lydfiler_L+R/8000Hz_1.mp3")
        pygame.mixer.music.play()
        time.sleep(10)
        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.1)
        lydstyrke = pygame.mixer.music.get_volume()
        bantal +=1

two_hundred_fifty()
time.sleep(10)
five_hundred()
time.sleep(10)
thousand()
time.sleep(10)
two_thousand()
time.sleep(10)
four_thousand()
time.sleep(10)
eight_thousand()
