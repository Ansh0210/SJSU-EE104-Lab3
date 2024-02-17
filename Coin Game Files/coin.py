# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 12:35:42 2023

@author: Nathan Lee
"""

import pgzrun
import pygame
import pgzero
from pgzero.builtins import Actor
from random import randint

#Introducing the Actors
fox = Actor("fox")
fox.pos = 100, 100

coin = Actor("coin")
coin.pos = 200, 200

WIDTH = 800             #Bigger Playing Area
HEIGHT = 600

score = 0
game_over = False


#Time to draw
def draw():
    screen.fill("green")
    fox.draw()
    coin.draw()
    screen.draw.text("Score: " + str(score), color="black", topleft=(10,10), fontsize=60)
    if game_over:
        screen.fill("pink")
        screen.draw("Final Score: " + str(score), topleft=(10,10), fontsize=60)


def place_coin():
    coin.x = randint(20, (WIDTH-20))
    coin.y = randint(20, (HEIGHT-20))

def time_up():
    global game_over
    game_over = True

def update():
    global score
    
    if keyboard.left:           #Increased Speed
        fox.x = fox.x - 6
    elif keyboard.right:
        fox.x = fox.x + 6
    elif keyboard.up:
        fox.y = fox.y - 6
    elif keyboard.down:
        fox.y = fox.y + 6
        
    coin_collected = fox.colliderect(coin)
    
    if coin_collected:
        score = score + 10
        place_coin()
    
clock.schedule(time_up, 1000.0) #Increased Time
place_coin()    
     


#Run it
pgzrun.go()