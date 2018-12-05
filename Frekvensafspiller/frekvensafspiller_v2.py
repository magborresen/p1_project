# Importer de nodvendige biblioteker
import pygame
import time

# Initier pygame, som er dimsen, som afspiller lydfilerne
pygame.mixer.init()
# Angiv start volumen



def increase_volume_R():
    Antal = 0
    for Antal in range (100):
        pygame.mixer.set_volume(0,pygame.mixer.music.get_volume() + 0.01)
        time.sleep(1)
        Antal +=1

def increase_volume_L():
    Antal = 0
    for Antal in range (100):
        pygame.mixer.set_volume(pygame.mixer.music.get_volume() + 0.01 , 0.0)
        time.sleep(1)
        Antal +=1



def two_hundred_fifty_R():
    lydstyrke = 0.0
    starttid = time.time()
    if knaptrykket():
        sluttid = time.time()
        resultattid = sluttid - starttid
        return resultattid
    else:
        sounda = pygame.mixer.Sound("Frekvensafspiller/Lydfiler/250Hz_1.mp3")
        sounda.play()
        pygame.mixer.set_volume(lydstyrke)
        increase_volume_R()

def two_hundred_fifty_L():
    lydstyrke = 0.0
    starttid = time.time()
    if knaptrykket():
        sluttid = time.time()
        resultattid = sluttid - starttid
        return resultattid
    else:
        sounda = pygame.mixer.Sound("Frekvensafspiller/Lydfiler/250Hz_1.mp3")
        sounda.play()
        pygame.mixer.set_volume(lydstyrke)
        increase_volume_L()



def five_hundred_R():
    lydstyrke = 0.0
    starttid = time.time()
    if knaptrykket():
        sluttid = time.time()
        resultattid = sluttid - starttid
        return resultattid
    else:
        sounda = pygame.mixer.Sound("Frekvensafspiller/Lydfiler/500Hz_1.mp3")
        sounda.play()
        pygame.mixer.set_volume(lydstyrke)
        increase_volume_R()

def five_hundred_L():
    lydstyrke = 0.0
    starttid = time.time()
    if knaptrykket():
        sluttid = time.time()
        resultattid = sluttid - starttid
        return resultattid
    else:
        sounda = pygame.mixer.Sound("Frekvensafspiller/Lydfiler/500Hz_1.mp3")
        sounda.play()
        pygame.mixer.set_volume(lydstyrke)
        increase_volume_L()

def thousand_R():
    lydstyrke = 0.0
    starttid = time.time()
    if knaptrykket():
        sluttid = time.time()
        resultattid = sluttid - starttid
        return resultattid
    else:
        sounda = pygame.mixer.Sound("Frekvensafspiller/Lydfiler/1000Hz_1.mp3")
        sounda.play()
        pygame.mixer.set_volume(lydstyrke)
        increase_volume_R()

def thousand_L():
    lydstyrke = 0.0
    starttid = time.time()
    if knaptrykket():
        sluttid = time.time()
        resultattid = sluttid - starttid
        return resultattid
    else:
        sounda = pygame.mixer.Sound("Frekvensafspiller/Lydfiler/1000Hz_1.mp3")
        sounda.play()
        pygame.mixer.set_volume(lydstyrke)
        increase_volume_L()

def two_thousand_R():
    lydstyrke = 0.0
    starttid = time.time()
    if knaptrykket():
        sluttid = time.time()
        resultattid = sluttid - starttid
        return resultattid
    else:
        sounda = pygame.mixer.Sound("Frekvensafspiller/Lydfiler/2000Hz_1.mp3")
        sounda.play()
        pygame.mixer.set_volume(lydstyrke)
        increase_volume_R()

def two_thousand_L():
    lydstyrke = 0.0
    starttid = time.time()
    if knaptrykket():
        sluttid = time.time()
        resultattid = sluttid - starttid
        return resultattid
    else:
        sounda = pygame.mixer.Sound("Frekvensafspiller/Lydfiler/2000Hz_1.mp3")
        sounda.play()
        pygame.mixer.set_volume(lydstyrke)
        increase_volume_L()

def four_thousand_R():
    lydstyrke = 0.0
    starttid = time.time()
    if knaptrykket():
        sluttid = time.time()
        resultattid = sluttid - starttid
        return resultattid
    else:
        sounda = pygame.mixer.Sound("Frekvensafspiller/Lydfiler/4000Hz_1.mp3")
        sounda.play()
        pygame.mixer.set_volume(lydstyrke)
        increase_volume_R()

def four_thousand_L():
    lydstyrke = 0.0
    starttid = time.time()
    if knaptrykket():
        sluttid = time.time()
        resultattid = sluttid - starttid
        return resultattid
    else:
        sounda = pygame.mixer.Sound("Frekvensafspiller/Lydfiler/4000Hz_1.mp3")
        sounda.play()
        pygame.mixer.set_volume(lydstyrke)
        increase_volume_L()

def eight_thousand_R():
    lydstyrke = 0.0
    starttid = time.time()
    if knaptrykket():
        sluttid = time.time()
        resultattid = sluttid - starttid
        return resultattid
    else:
        sounda = pygame.mixer.Sound("Frekvensafspiller/Lydfiler/8000Hz_1.mp3")
        sounda.play()
        pygame.mixer.set_volume(lydstyrke)
        increase_volume_R()

def eight_thousand_L():
    lydstyrke = 0.0
    starttid = time.time()
    if knaptrykket():
        sluttid = time.time()
        resultattid = sluttid - starttid
        return resultattid
    else:
        sounda = pygame.mixer.Sound("Frekvensafspiller/Lydfiler/8000Hz_1.mp3")
        sounda.play()
        pygame.mixer.set_volume(lydstyrke)
        increase_volume_L()



resultattid_two_hundred_fifty = two_hundred_fifty()
resultattid_five_hundred = five_hundred()
resultattid_thousand = thousand()
resultattid_two_thousand = two_thousand()
resultattid_four_thousand = four_thousand()
resultattid_eight_thousand = eight_thousand()

Person_one = [resultattid_two_hundred_fifty , resultattid_five_hundred , resultattid_thousand , resultattid_two_thousand , resultattid_four_thousand , resultattid_eight_thousand]
