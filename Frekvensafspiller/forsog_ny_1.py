import pyglet
import time


def play_right_ear(vol, freq, sec):
    volume = vol
    myplay = pyglet.media.Player()
    sound_file = "../Frekvensafspiller/justerede_lydfiler(A)/" + str(freq) + "Hz_R.wav"
    sound = pyglet.media.load(sound_file, streaming=False)
    myplay.queue(self.slowCaseSongSource)
    myplay.eos_action = 'loop'
    myplay.volume = volume
    myplay.play()
    time.sleep(sec)
    return(0)


def play_right_ear(vol, freq, sec):
    volume = vol
    myplay = pyglet.media.Player()
    sound_file = "../Frekvensafspiller/justerede_lydfiler(A)/" + str(freq) + "Hz_L.wav"
    sound = pyglet.media.load(sound_file, streaming=False)
    myplay.queue(self.slowCaseSongSource)
    myplay.eos_action = 'loop'
    myplay.volume = volume
    myplay.play()
    time.sleep(sec)
    return(0)

play_right_ear(0.5, 500, 10)
play_left_ear(0.5, 500, 10)
