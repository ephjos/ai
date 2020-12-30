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

