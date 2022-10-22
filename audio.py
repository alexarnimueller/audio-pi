#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pygame
import RPi.GPIO as GPIO

# define GPIO pins
b_play = 1  # play button (green)
b_next = 2  # next button (black)
b_prev = 3  # previous button (black)
l_gre = 4   # green LED (play)
l_red = 5   # red LED (pause)

# setup GPIO pins to IN or OUT mode with pulldown resistor
GPIO.setmode(GPIO.BOARD)
GPIO.setup(b_play, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(b_next, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(b_prev, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(l_gre, GPIO.OUT, pull_up_down=GPIO.PUD_DOWN)
# start red LED in HIGH state
GPIO.setup(l_red, GPIO.OUT, pull_up_down=GPIO.PUD_UP)

# code goes here
pygame.mixer.init()
sound = pygame.mixer.Sound('./audiofiles/ding.wav')
playing = sound.play()
while playing.get_busy():
    pygame.time.delay(100)

GPIO.cleanup()
sys.exit()
