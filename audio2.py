#! /usr/bin/env python
# -*- coding: utf-8 -*-

from gpiozero import Button, LED
from signal import pause 

# define GPIO pins
b_play = Button(16, pull_down=False)  # play button (green)
b_next = Button(20, pull_down=False)  # next button (black)
b_prev = Button(12, pull_down=False)  # previous button (black)
l_gre = LED(26)   # green LED (play)
l_red = LED(13)   # red LED (pause)

l_red.on()

def next(): 
    print("NEXT") 

def prev(): 
    print("PREVIOUS") 

def play():
    global l_gre, l_red
    l_red.off()
    l_gre.on()
    print("PLAY")

b_play.when_pressed = play 
b_next.when_pressed = next 
b_prev.when_pressed = prev 

pause()