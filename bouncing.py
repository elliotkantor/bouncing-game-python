#! ~/Desktop/Environmnets/pygames.venv/bin/python3
import pygame, sys
from pygame import *

pygame.init()
clock = pygame.time.Clock()

windowSize = (800, 600)
backgroundColor = (0,0,0)  # black
display = pygame.display.set_mode(windowSize)
pygame.display.set_caption("DVD Loading")
iconLocation = [50,50]
icon = pygame.Rect(iconLocation[0],iconLocation[1],150,100)
iconColor = 'red'
velocity = 2
direction = [1,1] # x and y (pos or neg)

def changeColor(currentColor):
    colorSequence = 'red purple yellow blue green orange'.split()
    currentIndex = colorSequence.index(currentColor)
    nextIndex = currentIndex + 1
    if nextIndex >= len(colorSequence):
        nextIndex = 0
    nextColor = colorSequence[nextIndex]
    return nextColor

running = True
while running:
    display.fill(backgroundColor)
    pygame.draw.rect(display, iconColor, icon)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            running = False
    
    # move it
    iconLocation[0] += velocity * direction[0]
    iconLocation[1] += velocity * direction[1]
    icon.x = iconLocation[0]
    icon.y = iconLocation[1]
    # check for collisions
    if iconLocation[0] < 0:
        iconLocation[0] = 0
        direction[0] *= -1
        iconColor = changeColor(iconColor)
    elif (iconLocation[0] + icon.w) > windowSize[0]:
        iconLocation[0] = windowSize[0] - icon.w
        direction[0] *= -1
        iconColor = changeColor(iconColor)

    if iconLocation[1] < 0:
        iconLocation[1] = 0
        direction[1] *= -1
        iconColor = changeColor(iconColor)
    elif (iconLocation[1] + icon.h) > windowSize[1]:
        iconLocation[1] = windowSize[1] - icon.h
        direction[1] *= -1
        iconColor = changeColor(iconColor)


    pygame.display.update()
    clock.tick(60) # fps 
