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

class SnakeGame():
    def __init__(self,
                 width=1000, height=500, fps=10, timestep=100,
                 board_size=15, tile_size=None, get_events=pygame.event.get):
        self.width = width
        self.height = height
        self.fps = fps
        self.board_size = board_size
        self.tile_size = tile_size if tile_size else height // board_size
        self.offset = (height - (self.tile_size*board_size)) // 2
        self.gap = 1
        self.get_events = get_events
        self.timestep = timestep

    def draw_tiles(self, surface, tiles):
        """Draw the board using appropriate tile size and gaps"""
        for (i,j), v in tiles.items():
            pygame.draw.rect(
                surface, v.to_color(),
                pygame.Rect(
                    (i*self.tile_size)+self.offset, (j*self.tile_size)+self.offset,
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
        self.tiles = {(i,j): Tile.Empty
                 for i in range(self.board_size)
                 for j in range(self.board_size)}
        y,x = int(self.board_size*0.25), self.board_size//2 # starting positions

        # Set initial food (fixed)
        food = (int(self.board_size*0.75), x)
        self.tiles[food] = Tile.Food

        snake_queue = Queue()
        self.head = (y,x) # follow self.head (know when to move next)
        direction = Direction.Right # start moving to the right
        for part in [(y-2,x),(y-1,x),(y,x)]: # initialize snake
            snake_queue.put(part)
            self.tiles[part] = Tile.Snake

        game_state = GameState.Running
        self.got_food = False
        self.score = 0
        max_score = (self.board_size**2)-3
        self.time = 0

        # Initial render
        surface.fill(Color.Black) # clear screen

        # draw current state
        self.draw_tiles(surface, self.tiles)
        screen.blit(surface, (0,0))
        pygame.display.flip()

        # enforce fps and screen update
        clock.tick(self.fps)
        pygame.display.update()

        while game_state == GameState.Running:
            # handle events
            for event in self.get_events():
                if event.type == pygame.QUIT:
                    game_state = GameState.Quit
                    break
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and \
                            direction != Direction.Down:
                        direction = Direction.Up
                        break
                    elif event.key == pygame.K_DOWN and \
                            direction != Direction.Up:
                        direction = Direction.Down
                        break
                    elif event.key == pygame.K_LEFT and \
                            direction != Direction.Right:
                        direction = Direction.Left
                        break
                    elif event.key == pygame.K_RIGHT and \
                            direction != Direction.Left:
                        direction = Direction.Right
                        break

            # game state updates
            next_head = (self.head[0]+direction[0],self.head[1]+direction[1])

            # Enforce board boundaries
            if not 0 <= next_head[0] < self.board_size or \
               not 0 <= next_head[1] < self.board_size:
                game_over = GameState.Loss
                break

            # Detect tail collision
            if self.tiles[next_head] == Tile.Snake:
                game_over = GameState.Loss
                break

            # Detect picking up food
            self.got_food = False
            if self.tiles[next_head] == Tile.Food:
                self.score += 1
                if self.score == max_score:
                    game_over = GameState.Win
                    break
                self.got_food = True # skip popping from tail, results in "growing"
                self.tiles[self.rand_point(self.tiles)] = Tile.Food

            # Add new self.head tile
            snake_queue.put(next_head)
            self.tiles[next_head] = Tile.Snake
            self.head = next_head
            if not self.got_food: # grow when food eaten, otherwise pop tail
                self.tiles[snake_queue.get_nowait()] = Tile.Empty

            # Update screen
            surface.fill(Color.Black) # clear screen

            # draw current state
            self.draw_tiles(surface, self.tiles)
            screen.blit(surface, (0,0))
            pygame.display.flip()

            # enforce fps and screen update
            clock.tick(self.fps)
            pygame.display.update()

            self.time += 1

        pygame.quit()



if __name__ == "__main__":
    sg = SnakeGame()
    sg.play()

