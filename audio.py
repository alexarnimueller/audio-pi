#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
from time import sleep
from pygame import mixer
from collections import deque
from gpiozero import Button, LED
from signal import pause 

# define GPIO pins
b_play = Button(16, pull_up=False)  # play button (green)
b_next = Button(20, pull_up=False)  # next button (black)
b_prev = Button(12, pull_up=False)  # previous button (black)
l_gre = LED(26)   # green LED (play)
l_red = LED(13)   # red LED (pause)

l_red.on()
l_gre.on()

audiodir = "/media/pi/AUDIO"  # "./audiofiles"
audiofiles = deque([f"{audiodir}/{f}" for f in os.listdir(f"{audiodir}") if not f.startswith('.')])

mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=1024)
mixer.init()
mixer.music.load(audiofiles[0])
mixer.music.play()
is_paused = False

def next():
    mixer.music.stop()
    audiofiles.rotate(-1)
    sleep(0.2)
    mixer.music.load(audiofiles[0])
    mixer.music.play()
    print("NEXT")

def prev():
    global is_paused
    if is_paused:
        mixer.music.play(start=0.0)
        print("RESTART")
    else:
        mixer.music.stop()
        audiofiles.rotate(1)
        sleep(0.5)
        mixer.music.load(audiofiles[0])
        mixer.music.play()
        print("PREVIOUS")

def play():
    global is_paused
    if mixer.music.get_busy() and not is_paused:
        mixer.music.pause()
        is_paused = True
        sleep(0.5)
        print("PAUSE")
    elif is_paused:
        mixer.music.unpause()
        is_paused = False
        print("CONTINUE")
    else:
        mixer.music.play()
        sleep(0.5)
        print("PLAY")

b_play.when_pressed = play 
b_next.when_pressed = next 
b_prev.when_pressed = prev 

pause()
