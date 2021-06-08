#! ~/Desktop/Environmnets/pygames.venv/bin/python3
import pygame, sys, random
from pygame import *

pygame.init()
clock = pygame.time.Clock()

windowSize = (800, 600)
backgroundColor = (0,0,0)  # black
display = pygame.display.set_mode(windowSize)
captions = ['DVD Loading', 'DVD Loading.', 'DVD Loading..','DVD Loading...']
currentCaption = captions[0]
pygame.display.set_caption(currentCaption)
# starting location
iconDimensions = (150,100)
iconLocation = [random.randint(0, windowSize[0] - iconDimensions[0]),random.randint(0, windowSize[1] - iconDimensions[1])]
icon = pygame.Rect(iconLocation[0],iconLocation[1],iconDimensions[0],iconDimensions[1])
defaultVelocity = 5
currentVelocity = defaultVelocity
colorSequence = 'red purple yellow blue green orange'.split()
iconColor = random.choice(colorSequence)
soundObj = pygame.mixer.Sound('click.wav')
frame = 1

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
def updateCaption(currentCaption):
    global captions
    currentIndex = captions.index(currentCaption)
    nextIndex = currentIndex + 1
    if nextIndex >= len(captions):
        nextIndex = 0
    nextCaption = captions[nextIndex]
    return nextCaption

running = True
while running:
    display.fill(backgroundColor)
    frame += 1
    if frame > 120:
        frame = 0
    if frame % 20 == 0:
        currentCaption = updateCaption(currentCaption)
        pygame.display.set_caption(currentCaption)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                running = False
            if event.key == pygame.K_SPACE and currentVelocity != 0:
                currentVelocity = 0
            elif event.key == pygame.K_SPACE and currentVelocity == 0:
                currentVelocity = defaultVelocity
            elif event.key == pygame.K_r:
                direction[0] *= -1
                direction[1] *= -1
    # move it
    icon.x += currentVelocity * direction[0]
    icon.y += currentVelocity * direction[1]
    # check for collisions
    if icon.x < 0:
        icon.x = 0
        direction[0] *= -1
        iconColor = randomColor(iconColor)
        soundObj.play()
    elif (icon.x + icon.w) > windowSize[0]:
        icon.x = windowSize[0] - icon.w
        direction[0] *= -1
        iconColor = randomColor(iconColor)
        soundObj.play()

    if icon.y < 0:
        icon.y = 0
        direction[1] *= -1
        iconColor = randomColor(iconColor)
        soundObj.play()
    elif (icon.y + icon.h) > windowSize[1]:
        icon.y = windowSize[1] - icon.h
        direction[1] *= -1
        iconColor = randomColor(iconColor)
        soundObj.play()

    pygame.draw.rect(display, iconColor, icon)
    pygame.display.update()
    clock.tick(60) # fps 
