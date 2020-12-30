#!/usr/bin/env python
from enum import Enum, auto

class Tile:
    Empty   = '-'
    X       = 'X'
    O       = 'O'

class Result(Enum):
    Tie     = auto()
    X_Win   = auto()
    O_Win   = auto()


def show_board(board):
    for i in range(3):
        i *= 3
        print(f'{board[i]} {board[i+1]} {board[i+2]}')
    print()
