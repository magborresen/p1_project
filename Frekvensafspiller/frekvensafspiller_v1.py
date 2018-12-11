# Importer de nodvendige biblioteker
import pygame
import time

# Initier pygame, som er dimsen, som afspiller lydfilerne
pygame.mixer.init()

#Setup til knappen



# Funktion, som faar lydstyrken til at stige
def increase_volume():
    New_volume = pygame.mixer.music.get_volume()
    pygame.mixer.music.set_volume(New_volume)
    Antal = 0
    for Antal in range (1):
        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.01)
        time.sleep(0.1)
        Antal +=1

def two_hundred_fifty_R():
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

def two_hundred_fifty_L():
    lydstyrke = 0.0
    starttid = time.time()
    for ten_loops in range(10):
        if knaptrykket():
            sluttid = time.time()
            resultattid = sluttid - starttid
            return resultattid
        else:
            pygame.mixer.music.load("Frekvensafspiller/Lydfiler/250Hz_1_L.mp3")
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(lydstyrke)
            increase_volume()
            lydstyrke = pygame.mixer.music.get_volume()

def five_hundred_R():
    lydstyrke = 0.0
    starttid = time.time()
    for ten_loops in range(10):
        if knaptrykket():
            sluttid = time.time()
            resultattid = sluttid - starttid
            return resultattid
        else:
            pygame.mixer.music.load("Frekvensafspiller/Lydfiler/500Hz_1_R.mp3")
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(lydstyrke)
            increase_volume()
            lydstyrke = pygame.mixer.music.get_volume()

def five_hundred_L():
    lydstyrke = 0.0
    starttid = time.time()
    for ten_loops in range(10):
        if knaptrykket():
            sluttid = time.time()
            resultattid = sluttid - starttid
            return resultattid
        else:
            pygame.mixer.music.load("Frekvensafspiller/Lydfiler/500Hz_1_L.mp3")
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(lydstyrke)
            increase_volume()
            lydstyrke = pygame.mixer.music.get_volume()

def thousand_R():
    lydstyrke = 0.0
    starttid = time.time()
    for ten_loops in range(10):
        if knaptrykket():
            sluttid = time.time()
            resultattid = sluttid - starttid
            return resultattid
        else:
            pygame.mixer.music.load("Frekvensafspiller/Lydfiler/1000Hz_1_R.mp3")
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(lydstyrke)
            increase_volume()
            lydstyrke = pygame.mixer.music.get_volume()

def thousand_L():
    lydstyrke = 0.0
    starttid = time.time()
    for ten_loops in range(10):
        if knaptrykket():
            sluttid = time.time()
            resultattid = sluttid - starttid
            return resultattid
        else:
            pygame.mixer.music.load("Frekvensafspiller/Lydfiler/1000Hz_1_L.mp3")
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(lydstyrke)
            increase_volume()
            lydstyrke = pygame.mixer.music.get_volume()

def two_thousand_R():
    lydstyrke = 0.0
    starttid = time.time()
    for ten_loops in range(10):
        if knaptrykket():
            sluttid = time.time()
            resultattid = sluttid - starttid
            return resultattid
        else:
            pygame.mixer.music.load("Frekvensafspiller/Lydfiler/2000Hz_1_R.mp3")
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(lydstyrke)
            increase_volume()
            lydstyrke = pygame.mixer.music.get_volume()

def two_thousand_L():
    lydstyrke = 0.0
    starttid = time.time()
    for ten_loops in range(10):
        if knaptrykket():
            sluttid = time.time()
            resultattid = sluttid - starttid
            return resultattid
        else:
            pygame.mixer.music.load("Frekvensafspiller/Lydfiler/2000Hz_1_L.mp3")
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(lydstyrke)
            increase_volume()
            lydstyrke = pygame.mixer.music.get_volume()

def four_thousand_R():
    lydstyrke = 0.0
    starttid = time.time()
    for ten_loops in range(10):
        if knaptrykket():
            sluttid = time.time()
            resultattid = sluttid - starttid
            return resultattid
        else:
            pygame.mixer.music.load("Frekvensafspiller/Lydfiler/4000Hz_1_R.mp3")
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(lydstyrke)
            increase_volume()
            lydstyrke = pygame.mixer.music.get_volume()

def four_thousand_L():
    lydstyrke = 0.0
    starttid = time.time()
    for ten_loops in range(10):
        if knaptrykket():
            sluttid = time.time()
            resultattid = sluttid - starttid
            return resultattid
        else:
            pygame.mixer.music.load("Frekvensafspiller/Lydfiler/4000Hz_1_L.mp3")
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(lydstyrke)
            increase_volume()
            lydstyrke = pygame.mixer.music.get_volume()

def eight_thousand_R():
    lydstyrke = 0.0
    starttid = time.time()
    for ten_loops in range(10):
        if knaptrykket():
            sluttid = time.time()
            resultattid = sluttid - starttid
            return resultattid
        else:
            pygame.mixer.music.load("Frekvensafspiller/Lydfiler/8000Hz_1_R.mp3")
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(lydstyrke)
            increase_volume()
            lydstyrke = pygame.mixer.music.get_volume()

def eight_thousand_L():
    lydstyrke = 0.0
    starttid = time.time()
    for ten_loops in range(10):
        if knaptrykket():
            sluttid = time.time()
            resultattid = sluttid - starttid
            return resultattid
        else:
            pygame.mixer.music.load("Frekvensafspiller/Lydfiler/8000Hz_1_L.mp3")
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(lydstyrke)
            increase_volume()
            lydstyrke = pygame.mixer.music.get_volume()

def the_test():
    resultattid_two_hundred_fifty_R = two_hundred_fifty_R()
    resultattid_five_hundred_R = five_hundred_R()
    resultattid_thousand_R = thousand_R()
    resultattid_two_thousand_R = two_thousand_R()
    resultattid_four_thousand_R = four_thousand_R()
    resultattid_eight_thousand_R = eight_thousand_R()

    resultattid_two_hundred_fifty_L = two_hundred_fifty_L()
    resultattid_five_hundred_L = five_hundred_L()
    resultattid_thousand_L = thousand_L()
    resultattid_two_thousand_L = two_thousand_L()
    resultattid_four_thousand_L = four_thousand_L()
    resultattid_eight_thousand_L = eight_thousand_L()


#First test subject
the_test()
Person_one_R = [resultattid_two_hundred_fifty_R , resultattid_five_hundred_R , resultattid_thousand_R , resultattid_two_thousand_R , resultattid_four_thousand_R , resultattid_eight_thousand_R]
Person_one_L = [resultattid_two_hundred_fifty_L , resultattid_five_hundred_L , resultattid_thousand_L , resultattid_two_thousand_L , resultattid_four_thousand_L , resultattid_eight_thousand_L]
Person_one = [Person_one_R , Person_one_L]
