#! /usr/bin/env python
# -*- coding: utf-8 -*-

from gpiozero import Button 
from signal import pause 

def next(): 
    print("NEXT") 

def prev(): 
    print("PREVIOUS") 

def play():
    print("PLAY")

# define GPIO pins
b_play = Button(16)  # play button (green)
b_next = Button(20)  # next button (black)
b_prev = Button(12)  # previous button (black)
l_gre = Button(26)   # green LED (play)
l_red = Button(13)   # red LED (pause)

b_play.when_pressed = play 
b_next.when_pressed = next 
b_prev.when_pressed = prev 

pause()