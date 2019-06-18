import numpy as np

ALPHA = 0.5
GAMMA = 0.5

ACTIONS = 4
MAX_STATES = 1000  # Max iterations

GRID_START = (0, 0)
GRID_END = (4, 4)

R_START, C_START = GRID_START
R_END, C_END = GRID_END

INITIAL_POS = (GRID_END[0]//2, GRID_END[1]//2)
REWARD_POS = GRID_END

initial_q = 0


class Position:
    def __init__(self, r, c):
        self.r = r
        self.c = c

    def up(self):
        if self.r == R_START:
            self.r = R_END
        else:
            self.r -= 1

    def down(self):
        if self.r == R_END:
            r = R_START
        else:
            self.r += 1

    def left(self):
        if self.c == C_START:
            self.c = C_END
        else:
            self.c -= 1

    def right(self):
        if self.c == C_END:
            self.c = C_START
        else:
            self.c += 1

    def __eq__(self, other):
        if isinstance(other, tuple):
            return (self.r, self.c) == other
        elif isinstance(other, type(self)):
            return self.r == other.r and self.c == other.c
        else:
            raise Exception(
                f'Cannot compare {type(self)} with {type(other)} objects')

    def get_tuple(self):
        return (self.r, self.c)

    def __repr__(self):
        return f'Position(r={self.r}, c={self.c})'

    def __str__(self):
        return f'({self.r}, {self.c})'


def get_reward(pos):
    if pos == REWARD_POS:
        return 1
    return 0


def update(q):
    pass


pos = (4, 4)
