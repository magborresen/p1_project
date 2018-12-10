# Importer de nodvendige biblioteker
import pygame
import time

# Initier pygame, som er dimsen, som afspiller lydfilerne
pygame.mixer.init()

#Afspil 250Hz
def two_hundred_fifty():
    print("250")
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.load("justerede_lydfiler/250Hz_1.mp3")
    pygame.mixer.music.play()

    time.sleep(10)

#Afspil 250Hz
def five_hundred():
    print("500")
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.load("justerede_lydfiler/500Hz_1.mp3")
    pygame.mixer.music.play()

    time.sleep(10)

#Afspil 250Hz
def thousand():
    print("1000")
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.load("justerede_lydfiler/1000Hz_1.mp3")
    pygame.mixer.music.play()

    time.sleep(10)

#Afspil 250Hz
def two_thousand():
    print("2000")
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.load("justerede_lydfiler/2000Hz_1.mp3")
    pygame.mixer.music.play()

    time.sleep(10)

#Afspil 250Hz
def four_thousand():
    print("4000")
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.load("justerede_lydfiler/4000Hz_1.mp3")
    pygame.mixer.music.play()

    time.sleep(10)

#Afspil 250Hz
def eight_thousand():
    print("8000")
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.load("justerede_lydfiler/8000Hz_1.mp3")
    pygame.mixer.music.play()

    time.sleep(10)

two_hundred_fifty()
five_hundred()
thousand()
two_thousand()
four_thousand()
eight_thousand()
