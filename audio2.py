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

audiodir = os.path.dirname(__file__) + "/audiofiles"
audiofiles = deque([f"{audiodir}/{f}" for f in os.listdir(f"{audiodir}")])

mixer.init()
mixer.music.load(audiofiles[0])
mixer.music.play(-1)

def next():
    mixer.music.stop()
    audiofiles.rotate(1)
    sleep(0.2)
    mixer.music.load(audiofiles[0])
    mixer.music.play()
    print("NEXT")

def prev():
    mixer.music.stop()
    audiofiles.rotate(-1)
    sleep(0.2)
    mixer.music.load(audiofiles[0])
    mixer.music.play()
    print("PREVIOUS") 

def play():
    l_red.off()
    l_gre.on()
    if mixer.music.get_busy():
        mixer.music.pause()
        print("PAUSE")
        sleep(0.2)
    else:
        mixer.music.unpause()
        print("PLAY")
        sleep(0.2)

b_play.when_pressed = play 
b_next.when_pressed = next 
b_prev.when_pressed = prev 

pause()