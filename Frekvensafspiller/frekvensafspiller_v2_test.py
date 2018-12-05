# Importer de nodvendige biblioteker
import pygame
import time

# Initier pygame, som er dimsen, som afspiller lydfilerne
pygame.mixer.init()
# Angiv start volumen
channel =


def increase_volume_R():
    Antal = 0
    lydstyrke_R = 0
    for Antal in range (100):
        pygame.mixer.Channel(channel).set_volume(0,lydstyrke_R + 0.3)
        time.sleep(1)
        Antal +=1
        lydstyrke_R = lydstyrke_R + 0.3

def increase_volume_L():
    Antal = 0
    for Antal in range (100):
        pygame.mixer.set_volume(pygame.mixer.get_volume() + 0.01 , 0.0)
        time.sleep(1)
        Antal +=1



def two_hundred_fifty_R():
    lydstyrke = 0.0
    starttid = time.time()
    pygame.mixer.Channel(channel)
    sounda = pygame.mixer.Sound("Frekvensafspiller/Lydfiler/250Hz_1.mp3")
    pygame.mixer.Channel(channel).play(sounda)
    pygame.mixer.Channel(channel).set_volume(lydstyrke)
    increase_volume_R()

two_hundred_fifty_R()
time.sleep(100)
