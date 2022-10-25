#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
from time import sleep
from pygame import mixer
from collections import deque
from gpiozero import Button, LED
from signal import pause 

# define GPIO pins
b_play = Button(16, pull_down=False)  # play button (green)
b_next = Button(20, pull_down=False)  # next button (black)
b_prev = Button(12, pull_down=False)  # previous button (black)
l_gre = LED(26)   # green LED (play)
l_red = LED(13)   # red LED (pause)
l_red.on()

audiofiles = deque([f"./audiofiles/{f}" for f in os.listdir("./audiofiles")])

mixer.init()
mixer.Sound(audiofiles[0])

def next():
    mixer.stop()
    audiofiles.rotate(1)
    sleep(0.25)
    mixer.Sound(audiofiles[0])
    print("NEXT")

def prev():
    mixer.stop()
    audiofiles.rotate(-1)
    sleep(0.25)
    mixer.Sound(audiofiles[0])
    print("PREVIOUS") 

def play():
    l_red.off()
    l_gre.on()
    if mixer.get_busy():
        mixer.pause()
        print("PAUSE")
    else:
        mixer.play()
        print("PLAY")

b_play.when_pressed = play 
b_next.when_pressed = next 
b_prev.when_pressed = prev 

pause()