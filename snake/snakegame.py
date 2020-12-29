#!/usr/bin/env python
import enum
import pygame
import random

class Color():
    Black = (0,0,0)
    Grey = (127,127,127)
    White = (255,255,255)
    Red = (200,0,0)
    Green = (0,200,0)
    Blue = (0,0,200)

class Tile(enum.Enum):
    Empty = enum.auto()
    Snake = enum.auto()
    Food = enum.auto()

def tile_color(tile):
    d = {
        Tile.Empty: Color.Grey,
        Tile.Snake: Color.Blue,
        Tile.Food: Color.Red,
    }
    return d[tile]

class SnakeGame:
    def __init__(self,
                 width=800, height=400, fps=60,
                 board_size=15, tile_size=None):
        self.width = width
        self.height = height
        self.fps = fps
        self.board_size = board_size
        self.tile_size = tile_size if tile_size else height//board_size
        self.offset = (height - (self.tile_size*board_size)) // 2
        self.gap = 1

    def draw_tiles(self, surface, tiles):
        for i in range(self.board_size):
            for j in range(self.board_size):
                pygame.draw.rect(
                    surface, tile_color(tiles[i][j]),
                    pygame.Rect(
                        i*self.tile_size, (j*self.tile_size)+self.offset,
                        self.tile_size-self.gap, self.tile_size-self.gap))

    def play(self):
        # Init pygame
        pygame.display.init()
        pygame.display.set_caption("SnakeGame")
        clock = pygame.time.Clock()

        screen = pygame.display.set_mode((self.width, self.height))
        surface = pygame.Surface((self.width, self.height))

        running = True

        # Init game objects
        default_tiles = [[Tile.Empty for _ in range(self.board_size)]
                 for _ in range(self.board_size)]
        food = (int(self.board_size*0.75), self.board_size//2)
        y,x = int(self.board_size*0.25), self.board_size//2
        snake = [(y,x),(y-1,x),(y-2,x)]

        while running:
            tiles = default_tiles.copy()
            tiles[food[0]][food[1]] = Tile.Food
            for ty,tx in snake:
                tiles[ty][tx] = Tile.Snake

            surface.fill(Color.Black)
            self.draw_tiles(surface, tiles)
            screen.blit(surface, (0,0))
            pygame.display.flip()


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            clock.tick(self.fps)
            pygame.display.update()

        pygame.quit()



if __name__ == "__main__":
    sg = SnakeGame()
    sg.play()

