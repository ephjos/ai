#!/usr/bin/env python
import random
from common import Tile, Result, show_board

class Agent:
    def __init__(self):
        raise NotImplementedError('Cannot use abstract Agent')

    def get_move(self, board):
        raise NotImplementedError('Cannot use abstract Agent')

    def game_over(self, board, res):
        raise NotImplementedError('Cannot use abstract Agent')

    def set_tile(self, tile):
        self.tile = tile

class RandomChoice(Agent):
    name = 'RandomChoice'
    def __init__(self):
        return

    def get_move(self, board):
        return random.choice(
            [i for i,t in enumerate(board) if t == Tile.Empty])

    def game_over(self, board, res):
        return

class QLearning(Agent):
    name = 'QLearning'
    def __init__(self):
        self.Q = {}
        self.alpha = 0.9
        self.gamma = 0.3
        self.eps  = 0.05
        self.history = []

    def hash_state(self, board):
        return hash(''.join(board))

    def get_move(self, board):
        # TODO: on train only
        if random.random() < self.eps: # chance to make a random move
            return random.choice(
                [i for i,t in enumerate(board) if t == Tile.Empty])

        s_t = board.copy()
        hash_s_t = self.hash_state(s_t)

        # Never seen, initialize table entry
        if hash_s_t not in self.Q:
            self.Q[hash_s_t] = [0 if t == Tile.Empty else None
                           for i,t in enumerate(s_t)]

        # Pick action, randomly picking in case of tie
        m = max([v for v in self.Q[hash_s_t] if v is not None])
        a_t = random.choice(
            [i for i,a in enumerate(self.Q[hash_s_t]) if a == m])

        self.history.append((hash_s_t, a_t))

        return a_t

    def game_over(self, board, res):
        # Calculate reward based on result of game
        reward = -1
        if res == Result.Tie: reward = 0
        elif res == Result.X_Win and self.tile == Tile.X: reward = 1
        elif res == Result.O_Win and self.tile == Tile.O: reward = 1

        # Init next_state (state that happens when action is taken
        next_state = self.hash_state(board)
        if next_state not in self.Q:
            self.Q[next_state] = [0]

        # Go back over move history and update Q table
        while self.history:
            state, a = self.history.pop(-1)

            # Max of next_state
            maxQ_next = max([v for v in self.Q[next_state] if v is not None])

            # Bellman Equation
            self.Q[state][a] += self.alpha * \
                (reward + self.gamma * maxQ_next - self.Q[state][a])

            # Set values for next iteration
            next_state = state
            reward = self.Q[state][a]
        self.history = []

if __name__ == "__main__":
    print()

