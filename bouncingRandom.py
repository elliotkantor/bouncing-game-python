#! ~/Desktop/Environmnets/pygames.venv/bin/python3
import pygame, sys, random
from pygame import *

pygame.init()
clock = pygame.time.Clock()

windowSize = (800, 600)
backgroundColor = (0,0,0)  # black
display = pygame.display.set_mode(windowSize)
pygame.display.set_caption("DVD Loading...")
# starting location
iconDimensions = (150,100)
iconLocation = [random.randint(0, windowSize[0] - iconDimensions[0]),random.randint(0, windowSize[1] - iconDimensions[1])]
icon = pygame.Rect(iconLocation[0],iconLocation[1],iconDimensions[0],iconDimensions[1])
velocity = 5
colorSequence = 'red purple yellow blue green orange'.split()
iconColor = random.choice(colorSequence)
def randomDirection():
    '''Randomly returns + or - 1 to determine random direction of motion'''
    if random.randint(0,1) == 1:
        return 1
    else:
        return -1
direction = [randomDirection(),randomDirection()] # x and y (pos or neg)

def changeColor(currentColor):
    colorSequence = 'red purple yellow blue green orange'.split()
    currentIndex = colorSequence.index(currentColor)
    nextIndex = currentIndex + 1
    if nextIndex >= len(colorSequence):
        nextIndex = 0
    nextColor = colorSequence[nextIndex]
    return nextColor

def randomColor(currentColor):
    colorSequence = 'red purple yellow blue green orange'.split()
    # must switch colors, but it can be random
    del colorSequence[colorSequence.index(currentColor)]
    nextColor = random.choice(colorSequence)
    return nextColor
def getRandColor():
    # returns completely random color
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    return (red,green,blue)

running = True
while running:
    display.fill(backgroundColor)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            running = False
        if event.type == pygame.KEYDOWN:
            pass
    # move it
    icon.x += velocity * direction[0]
    icon.y += velocity * direction[1]
    # check for collisions
    if icon.x < 0 or (icon.x + icon.w) > windowSize[0]:
        direction[0] *= -1
        iconColor = getRandColor()

    if icon.y < 0 or (icon.y + icon.h) > windowSize[1]:
        direction[1] *= -1
        iconColor = getRandColor()
    pygame.draw.rect(display, iconColor, icon)
    pygame.display.update()
    clock.tick(60) # fps 
