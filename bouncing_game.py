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
        self.velocity = self.magnitude
        self.color_sequence = "red purple yellow blue green orange".split()
        self.color = random.choice(color_sequence)
        self.click_sound = pygame.mixer.Sound("click.wav")

    def update(self):

        self.x += self.velocity * self.direction[0]
        self.y += self.velocity * self.direction[1]

        # check for collisions
        if self.x < 0:
            self.x = 0
            self.direction[0] *= -1
            self.color = self.change_color(self.color)
            self.click_sound.play()
        elif (self.x + self.w) > windowSize[0]:
            self.x = windowSize[0] - self.w
            self.direction[0] *= -1
            self.color = self.change_color(self.color)
            self.click_sound.play()

        if self.y < 0:
            self.y = 0
            self.direction[1] *= -1
            self.color = self.change_color(self.color)
            self.click_sound.play()
        elif (self.y + self.h) > windowSize[1]:
            self.y = windowSize[1] - self.h
            self.direction[1] *= -1
            self.color = self.change_color(self.color)
            self.click_sound.play()

    def draw(self):
        pygame.draw.rect(
            display, self.color, pygame.Rect(self.x, self.y, self.w, self.h)
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
        next_color = self.color_sequence[nextIndex]
        return next_color


class RandomPaletteBlock(Block):
    def change_color(self, current_color) -> str:
        # must switch colors, but it can be random
        next_color = random.choice(
            [c for c in self.color_sequence if c != current_color]
        )
        return next_color


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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                running = False
            if event.key == pygame.K_SPACE and block.velocity != 0:
                block.velocity = 0
            elif event.key == pygame.K_SPACE and block.velocity == 0:
                block.velocity = block.magnitude
            elif event.key == pygame.K_r:
                block.direction[0] *= -1
                block.direction[1] *= -1

    # remove error when quitting
    try:
        pygame.display.update()
    except pygame.error:
        pass
    clock.tick(60)
