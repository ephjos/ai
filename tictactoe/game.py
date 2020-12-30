#!/usr/bin/env python
from agent import Agent, RandomChoice
import os
from common import Result, Tile
import time

class TicTacToeGame:
    def __init__(
            self,
            player_1: Agent,
            player_2: Agent,
    ):
        self.board = [Tile.Empty for _ in range(9)]
        self.player_1 = player_1
        self.player_2 = player_2

    def show_board(self):
        for i in range(3):
            i *= 3
            print(f'{self.board[i]} {self.board[i+1]} {self.board[i+2]}')
        print()

    def is_win(self):
        r1 = self.board[0] != Tile.Empty and \
            self.board[0] == self.board[1] == self.board[2]
        r2 = self.board[3] != Tile.Empty and \
            self.board[3] == self.board[4] == self.board[5]
        r3 = self.board[6] != Tile.Empty and \
            self.board[6] == self.board[7] == self.board[8]
        c1 = self.board[0] != Tile.Empty and \
            self.board[0] == self.board[3] == self.board[6]
        c2 = self.board[1] != Tile.Empty and \
            self.board[1] == self.board[4] == self.board[7]
        c3 = self.board[2] != Tile.Empty and \
            self.board[2] == self.board[5] == self.board[8]
        d1 = self.board[0] != Tile.Empty and \
            self.board[0] == self.board[4] == self.board[8]
        d2 = self.board[2] != Tile.Empty and \
            self.board[2] == self.board[4] == self.board[6]
        return r1 | r2 | r3 | c1 | c2 | c3 | d1 | d2

    def play(self):
        self.board = [Tile.Empty for _ in range(9)]
        i = 0
        self.player_1.set_tile(Tile.X)
        self.player_2.set_tile(Tile.O)
        while Tile.Empty in self.board and not self.is_win():
            #self.show_board()
            if i % 2 == 0:
                char = Tile.X
                move = self.player_1.get_move(self.board, char)
            else:
                char = Tile.O
                move = self.player_2.get_move(self.board, char)

            if self.board[move] != Tile.Empty:
                raise Exception('Trying to pick non-empty tile')

            self.board[move] = char
            i += 1

        #self.show_board()
        res = None
        if Tile.Empty not in self.board and not self.is_win():
            res = Result.Tie
        elif i % 2 == 0:
            res = Result.O_Win
        else:
            res = Result.X_Win

        if res is None:
            raise Exception('Error: Unknown termination')

        self.player_1.game_over(self.board, res)
        self.player_2.game_over(self.board, res)
        return res

if __name__ == "__main__":
    tttg = TicTacToeGame(RandomChoice(), RandomChoice())
    print(tttg.play())

