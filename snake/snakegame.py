#!/usr/bin/env python
import enum
import pygame
from queue import Queue
from random import randint

class Color():
    Black    = (0,   0,   0)
    Grey     = (127, 127, 127)
    White    = (255, 255, 255)
    Red      = (200, 0,   0)
    Green    = (0,   200, 0)
    Blue     = (0,   0,   200)

class Tile(enum.Enum):
    Empty    = enum.auto()
    Snake    = enum.auto()
    Food     = enum.auto()

    def to_color(self):
        d = {
            Tile.Empty:    Color.Grey,
            Tile.Snake:    Color.Blue,
            Tile.Food:     Color.Red,
        }
        return d[self]

class Direction():
    Up       = ( 0,-1)
    Down     = ( 0, 1)
    Left     = (-1, 0)
    Right    = ( 1, 0)

class GameState(enum.Enum):
    Running  = enum.auto()
    Win      = enum.auto()
    Loss     = enum.auto()
    Quit     = enum.auto()

class SnakeGame:
    def __init__(self,
                 width=1000, height=500, fps=10,
                 board_size=19, tile_size=None):
        self.width = width
        self.height = height
        self.fps = fps
        self.board_size = board_size
        self.tile_size = tile_size if tile_size else height//board_size
        self.offset = (height - (self.tile_size*board_size)) // 2
        self.gap = 1

    def draw_tiles(self, surface, tiles):
        """Draw the board using appropriate tile size and gaps"""
        for (i,j), v in tiles.items():
            pygame.draw.rect(
                surface, v.to_color(),
                pygame.Rect(
                    i*self.tile_size, (j*self.tile_size)+self.offset,
                    self.tile_size-self.gap, self.tile_size-self.gap))

    def rand_point(self, tiles):
        """Randomly pick an empty point on the board"""
        empty_points = [k for k,v in tiles.items() if v == Tile.Empty]
        l = len(empty_points)-1
        return empty_points[randint(0,l)]

    def play(self):
        # Init pygame
        pygame.display.init() # only need display
        pygame.display.set_caption("SnakeGame")
        clock = pygame.time.Clock() # initialize clock for enforcing fps

        # We render to a surface that is blit'd to the screen
        screen = pygame.display.set_mode((self.width, self.height))
        surface = pygame.Surface((self.width, self.height))

        # Init game objects
        tiles = {(i,j): Tile.Empty
                 for i in range(self.board_size)
                 for j in range(self.board_size)}
        y,x = int(self.board_size*0.25), self.board_size//2 # starting positions

        # Set initial food (fixed)
        food = (int(self.board_size*0.75), x)
        tiles[food] = Tile.Food

        snake_queue = Queue()
        head = (y,x) # follow head (know when to move next)
        direction = Direction.Right # start moving to the right
        for part in [(y-2,x),(y-1,x),(y,x)]: # initialize snake
            snake_queue.put(part)
            tiles[part] = Tile.Snake

        game_state = GameState.Running
        got_food = False
        last_tick = pygame.time.get_ticks()

        while game_state == GameState.Running:
            # handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = GameState.Quit
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and \
                            direction != Direction.Down:
                        direction = Direction.Up
                    if event.key == pygame.K_DOWN and \
                        direction != Direction.Up:
                        direction = Direction.Down
                    if event.key == pygame.K_LEFT and \
                            direction != Direction.Right:
                        direction = Direction.Left
                    if event.key == pygame.K_RIGHT and \
                            direction != Direction.Left:
                        direction = Direction.Right

            surface.fill(Color.Black) # clear screen

            # draw current state
            self.draw_tiles(surface, tiles)
            screen.blit(surface, (0,0))
            pygame.display.flip()

            # enforce fps and screen update
            clock.tick(self.fps)
            pygame.display.update()

            # game state updates
            next_head = (head[0]+direction[0],head[1]+direction[1])

            # Enforce board boundaries
            if not 0 <= next_head[0] < self.board_size or \
               not 0 <= next_head[1] < self.board_size:
                game_over = GameState.Loss
                # TODO: Handle score
                break

            # Detect tail collision
            if tiles[next_head] == Tile.Snake:
                game_over = GameState.Loss
                # TODO: Handle score
                break

            # Detect picking up food
            if tiles[next_head] == Tile.Food:
                got_food = True # skip popping from tail, results in "growing"
                tiles[self.rand_point(tiles)] = Tile.Food
                # TODO: Handle score

            snake_queue.put(next_head)
            tiles[next_head] = Tile.Snake
            head = next_head
            if not got_food:
                tiles[snake_queue.get_nowait()] = Tile.Empty
            got_food = False

        pygame.quit()



if __name__ == "__main__":
    sg = SnakeGame()
    sg.play()

