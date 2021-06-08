#! ~/Desktop/Environments/pygames.venv/bin/activate
import pygame
import random
from pygame import *


pygame.init()
clock = pygame.time.Clock()

windowSize = (800, 600)
backgroundColor = (0, 0, 0)  # black
display = pygame.display.set_mode(windowSize)
captions = ["DVD Loading", "DVD Loading.", "DVD Loading..", "DVD Loading..."]
currentCaption = captions[0]
pygame.display.set_caption(currentCaption)

color_sequence = "red purple yellow blue green orange".split()
iconColor = random.choice(color_sequence)
soundObj = pygame.mixer.Sound("click.wav")
frame = 1


def updateCaption(currentCaption):
    global captions
    current_index = captions.index(currentCaption)
    nextIndex = current_index + 1
    if nextIndex >= len(captions):
        nextIndex = 0
    nextCaption = captions[nextIndex]
    return nextCaption


class Block:
    def __init__(self):
        self.dimensions = (150, 100)
        self.position = [
            random.randint(0, windowSize[0] - self.dimensions[0]),
            random.randint(0, windowSize[1] - self.dimensions[1]),
        ]
        self.w = self.dimensions[0]
        self.h = self.dimensions[1]
        self.x = self.position[0]
        self.y = self.position[1]

        self.direction = [self.random_direction(), self.random_direction()]
        self.magnitude = 5
        self.color_sequence = "red purple yellow blue green orange".split()

    def update(self):

        self.x += self.magnitude * self.direction[0]
        self.y += self.magnitude * self.direction[1]

        # check for collisions
        if self.x < 0:
            self.x = 0
            self.direction[0] *= -1
            iconColor = self.randomColor(iconColor)
            soundObj.play()
        elif (self.x + self.w) > windowSize[0]:
            self.x = windowSize[0] - self.w
            self.direction[0] *= -1
            iconColor = self.randomColor(iconColor)
            soundObj.play()

        if self.y < 0:
            self.y = 0
            self.direction[1] *= -1
            iconColor = self.randomColor(iconColor)
            soundObj.play()
        elif (self.y + self.h) > windowSize[1]:
            self.y = windowSize[1] - self.h
            self.direction[1] *= -1
            iconColor = self.randomColor(iconColor)
            soundObj.play()

    def draw(self):
        # display.blit(pygame.Rect(100, 100, 100, 100))
        pygame.draw.rect(
            display, iconColor, pygame.Rect(self.x, self.y, self.w, self.h)
        )

    def random_direction(self):
        """Randomly returns + or - 1 to determine random self.direction of motion"""
        if random.randint(0, 1):
            return 1
        return -1


class SequentialColorBlock(Block):
    def change_color(self, current_color) -> str:
        current_index = self.color_sequence.index(current_color)
        nextIndex = current_index + 1
        if nextIndex >= len(self.color_sequence):
            nextIndex = 0
        nextColor = self.color_sequence[nextIndex]
        return nextColor


class RandomPaletteBlock(Block):
    def change_color(self, current_color) -> str:
        # must switch colors, but it can be random
        nextColor = random.choice([c for c in self.color_sequence if c != current_color])
        return nextColor


class RandomColorBlock(Block):
    def change_color(self) -> tuple:
        # returns completely random color
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        return (red, green, blue)


block = RandomPaletteBlock()
running = True
while running:
    display.fill(backgroundColor)
    block.update()
    block.draw()

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
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_ESCAPE:
        #         pygame.quit()
        #         running = False
        #     if event.key == pygame.K_SPACE and currentVelocity != 0:
        #         currentVelocity = 0
        #     elif event.key == pygame.K_SPACE and currentVelocity == 0:
        #         currentVelocity = defaultVelocity
        #     elif event.key == pygame.K_r:
        #         self.direction[0] *= -1
        #         self.direction[1] *= -1
    # move it
    pygame.display.update()
    clock.tick(60)  # fps
