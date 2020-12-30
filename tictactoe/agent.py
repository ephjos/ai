#!/usr/bin/env python
import random
from common import Tile, Result

################################################################################
import sys
################################################################################

class Agent:
    def __init__(self):
        raise NotImplementedError('Cannot use abstract Agent')

    def get_move(self, board, char):
        raise NotImplementedError('Cannot use abstract Agent')

    def game_over(self, board, res):
        raise NotImplementedError('Cannot use abstract Agent')

    def set_tile(self, tile):
        self.tile = tile

class RandomChoice(Agent):
    name = 'RandomChoice'
    def __init__(self):
        return

    def get_move(self, board, char):
        return random.choice(
            [i for i,t in enumerate(board) if t == Tile.Empty])

    def game_over(self, board, res):
        return

class QLearning(Agent):
    name = 'QLearning'
    def __init__(self):
        self.Q = {}
        self.alpha = 0.1
        self.gamma = 0.4

    def hash_state(self, board):
        return hash(tuple(board))

    def get_move(self, board, char):
        s_t = board.copy()
        old = self.hash_state(s_t)

        # Never seen, initialize table entry
        if old not in self.Q:
            self.Q[old] = [0 if t == Tile.Empty else -2**32
                           for i,t in enumerate(s_t)]

        # Pick action, randomly picking in case of tie
        m = max(self.Q[old])
        a_t = random.choice(
            [i for i,a in enumerate(self.Q[old]) if a == m])

        # State if action is taken
        s_tp1 = s_t.copy()
        s_tp1[a_t] = char
        new = self.hash_state(s_t)

        # Never seen, initialize table entry
        if new not in self.Q:
            self.Q[new] = [0 if t == Tile.Empty else -2**32
                           for i,t in enumerate(s_tp1)]

        maxQ = max(self.Q[new])

        self.Q[new][a_t] = self.Q[old][a_t] + self.alpha * \
            (self.gamma * maxQ - self.Q[old][a_t])

        self.last_action = a_t
        return a_t

    def game_over(self, board, res):
        s = board.copy()
        s[self.last_action] = Tile.Empty
        key = self.hash_state(s)
        reward = 0
        if res == Result.Tie:
            reward = 0.5
        elif res == Result.X_Win:
            if self.tile == Tile.X:
                reward = 1
            else:
                reward = -1
        elif res == Result.O_Win:
            if self.tile == Tile.O:
                reward = 1
            else:
                reward = -1

        if key not in self.Q:
            self.Q[key] = [0 if t == Tile.Empty else -2**32
                           for i,t in enumerate(s)]
        self.Q[key][self.last_action] = reward

if __name__ == "__main__":
    print()

