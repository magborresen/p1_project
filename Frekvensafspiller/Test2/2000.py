import pyglet
import time

def play_first():
    print("0,1")
    volume = 0.1
    player = pyglet.media.Player()
    sound_file = "../justerede_lydfiler(A)/2000Hz.wav"
    sound = pyglet.media.load(sound_file, streaming=False)
    looper = pyglet.media.SourceGroup(sound.audio_format, None)
    looper.loop = True
    looper.queue(sound)
    #pygame.mixer.music.load("../Frekvensafspiller/justerede_lydfiler/" + str(self.frequency) + "Hz_R.mp3")
    #pygame.mixer.music.play(10)

    #pygame.mixer.music.set_volume(volume)
    player.volume = volume
    player.queue(looper)
    player.play()
    time.sleep(30)

def play_second():
    print("0,2")
    volume = 0.2
    player = pyglet.media.Player()
    sound_file = "../justerede_lydfiler(A)/2000Hz.wav"
    sound = pyglet.media.load(sound_file, streaming=False)
    looper = pyglet.media.SourceGroup(sound.audio_format, None)
    looper.loop = True
    looper.queue(sound)
    #pygame.mixer.music.load("../Frekvensafspiller/justerede_lydfiler/" + str(self.frequency) + "Hz_R.mp3")
    #pygame.mixer.music.play(10)

    #pygame.mixer.music.set_volume(volume)
    player.volume = volume
    player.queue(looper)
    player.play()
    time.sleep(30)

def play_third():
    print("0,3")
    volume = 0.3
    player = pyglet.media.Player()
    sound_file = "../justerede_lydfiler(A)/2000Hz.wav"
    sound = pyglet.media.load(sound_file, streaming=False)
    looper = pyglet.media.SourceGroup(sound.audio_format, None)
    looper.loop = True
    looper.queue(sound)
    #pygame.mixer.music.load("../Frekvensafspiller/justerede_lydfiler/" + str(self.frequency) + "Hz_R.mp3")
    #pygame.mixer.music.play(10)

    #pygame.mixer.music.set_volume(volume)
    player.volume = volume
    player.queue(looper)
    player.play()
    time.sleep(30)

def play_fourth():
    print("0,4")
    volume = 0.4
    player = pyglet.media.Player()
    sound_file = "../justerede_lydfiler(A)/2000Hz.wav"
    sound = pyglet.media.load(sound_file, streaming=False)
    looper = pyglet.media.SourceGroup(sound.audio_format, None)
    looper.loop = True
    looper.queue(sound)
    #pygame.mixer.music.load("../Frekvensafspiller/justerede_lydfiler/" + str(self.frequency) + "Hz_R.mp3")
    #pygame.mixer.music.play(10)

    #pygame.mixer.music.set_volume(volume)
    player.volume = volume
    player.queue(looper)
    player.play()
    time.sleep(30)

def play_fifth():
    print("0,5")
    volume = 0.5
    player = pyglet.media.Player()
    sound_file = "../justerede_lydfiler(A)/2000Hz.wav"
    sound = pyglet.media.load(sound_file, streaming=False)
    looper = pyglet.media.SourceGroup(sound.audio_format, None)
    looper.loop = True
    looper.queue(sound)
    #pygame.mixer.music.load("../Frekvensafspiller/justerede_lydfiler/" + str(self.frequency) + "Hz_R.mp3")
    #pygame.mixer.music.play(10)

    #pygame.mixer.music.set_volume(volume)
    player.volume = volume
    player.queue(looper)
    player.play()
    time.sleep(30)

def play_sixth():
    print("0,6")
    volume = 0.6
    player = pyglet.media.Player()
    sound_file = "../justerede_lydfiler(A)/2000Hz.wav"
    sound = pyglet.media.load(sound_file, streaming=False)
    looper = pyglet.media.SourceGroup(sound.audio_format, None)
    looper.loop = True
    looper.queue(sound)
    #pygame.mixer.music.load("../Frekvensafspiller/justerede_lydfiler/" + str(self.frequency) + "Hz_R.mp3")
    #pygame.mixer.music.play(10)

    #pygame.mixer.music.set_volume(volume)
    player.volume = volume
    player.queue(looper)
    player.play()
    time.sleep(30)

def play_seventh():
    print("0,7")
    volume = 0.7
    player = pyglet.media.Player()
    sound_file = "../justerede_lydfiler(A)/2000Hz.wav"
    sound = pyglet.media.load(sound_file, streaming=False)
    looper = pyglet.media.SourceGroup(sound.audio_format, None)
    looper.loop = True
    looper.queue(sound)
    #pygame.mixer.music.load("../Frekvensafspiller/justerede_lydfiler/" + str(self.frequency) + "Hz_R.mp3")
    #pygame.mixer.music.play(10)

    #pygame.mixer.music.set_volume(volume)
    player.volume = volume
    player.queue(looper)
    player.play()
    time.sleep(30)

def play_eighth():
    print("0,8")
    volume = 0.8
    player = pyglet.media.Player()
    sound_file = "../justerede_lydfiler(A)/2000Hz.wav"
    sound = pyglet.media.load(sound_file, streaming=False)
    looper = pyglet.media.SourceGroup(sound.audio_format, None)
    looper.loop = True
    looper.queue(sound)
    #pygame.mixer.music.load("../Frekvensafspiller/justerede_lydfiler/" + str(self.frequency) + "Hz_R.mp3")
    #pygame.mixer.music.play(10)

    #pygame.mixer.music.set_volume(volume)
    player.volume = volume
    player.queue(looper)
    player.play()
    time.sleep(30)

def play_nineth():
    print("0,9")
    volume = 0.9
    player = pyglet.media.Player()
    sound_file = "../justerede_lydfiler(A)/2000Hz.wav"
    sound = pyglet.media.load(sound_file, streaming=False)
    looper = pyglet.media.SourceGroup(sound.audio_format, None)
    looper.loop = True
    looper.queue(sound)
    #pygame.mixer.music.load("../Frekvensafspiller/justerede_lydfiler/" + str(self.frequency) + "Hz_R.mp3")
    #pygame.mixer.music.play(10)

    #pygame.mixer.music.set_volume(volume)
    player.volume = volume
    player.queue(looper)
    player.play()
    time.sleep(30)

play_first()
play_second()
play_third()
play_fourth()
play_fifth()
play_sixth()
play_seventh()
play_eighth()
play_nineth()
