#!/usr/bin/env python
import pygame
from snakegame import *

class Event():
    Up      = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_UP)
    Down    = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_DOWN)
    Left    = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_LEFT)
    Right   = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RIGHT)

class Model():
    def __init__(self):
        #TODO: init table
        pass

    def create_events(self):
        return []

    def play(self):
        self.game = SnakeGame(get_events=self.create_events)
        self.game.play()

if __name__ == "__main__":
    model = Model()
    model.play()

