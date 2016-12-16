import RPi.GPIO as GPIO
import time
import vlc

GPIO.setmode(GPIO.BCM)

# Strands of Christmas lights
strand_1 = 2
strand_2 = 3
strand_3 = 4
strand_4 = 14

all_lights = [
    strand_1,
    strand_2,
    strand_3,
    strand_4,
]

BPM = 110
BEAT_IN_SECONDS = BPM/60.0

song_path = './christmas_song.mp3'

def setup_lights(lights):
    for light in lights:
        GPIO.setup(light, GPIO.OUT, initial=GPIO.LOW)

def start_song(song):
    p = vlc.MediaPlayer("file://" + song)
    p.play()

def start_lights:
    set_scene([strand_1, strand_2], [strand_3, strand_4], 4)

# steady_on: An array for the lights that will be steadily on for this scene
# flashing:  An array for the lights that will be flashing (once per beat) for this scene
# beats:     The number of beats to hold the scene for
def set_scene(steady_on, flashing, beats):
    clear_lights(all_lights)


def clear_lights(lights:
    for light in lights:
        turn_off(light)

def turn_on:

def turn_off:

setup_lights(all_lights)

start_song(song_path)
