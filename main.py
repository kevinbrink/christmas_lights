import RPi.GPIO as GPIO
import time
#import vlc

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

def start_lights():
    set_scene([strand_1, strand_2], [strand_3, strand_4], 4)
    set_scene([strand_3, strand_4], [strand_1, strand_2], 4)
    set_scene([strand_1, strand_2], [strand_3, strand_4], 2)
    set_scene([strand_3, strand_4], [strand_1, strand_2], 2)
    set_scene([], [], 4)
    set_scene([], [strand_3, strand_4], 4)
    set_scene([], [strand_1, strand_2], 4)

# steady_on: An array for the lights that will be steadily on for this scene
# flashing:  An array for the lights that will be flashing (once per beat) for this scene
# beats:     The number of beats to hold the scene for
def set_scene(steady_on, flashing, beats):
    # Clear out ALL lights
    clear_lights(all_lights)
    # Turn on all the steady lights
    for light in steady_on:
        turn_on(light)
    operation = turn_on

    # For each of the beats...
    for i in range(beats):
        # Turn each of them on
        for light in flashing:
            operation(light)

        # Sleep for a beat
        time.sleep(BEAT_IN_SECONDS)
        # Switch the operation for the next beat
        if operation == turn_off:
            operation = turn_on
        else:
            operation = turn_off

def clear_lights(lights):
    for light in lights:
        turn_off(light)

def turn_on(light):
    GPIO.output(light, GPIO.HIGH)

def turn_off(light):
    GPIO.output(light, GPIO.LOW)

setup_lights(all_lights)

# start_song(song_path)

start_lights()
