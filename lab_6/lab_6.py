import sys
import itertools
import numpy as np
from collections import defaultdict

ALPHA = 0.5  # Learning rate
GAMMA = 0.5  # Discount Factor

ACTIONS = 4  # up, down, left, right
MAX_ITERATIONS = 1000  # Max iterations

GRID_START = (0, 0)
GRID_END = (100, 100)
R_START, C_START = GRID_START
R_END, C_END = GRID_END

INITIAL_POS = (R_END//2, C_END//2)
REWARD_POS = GRID_END


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
            self.r = R_START
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

    def move(self, i):
        """0: up, 1: down, 2: left, 3: right"""
        if i == 0:
            self.up()
        elif i == 1:
            self.down()
        elif i == 2:
            self.left()
        else:
            self.right()

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


def get_max_action(actions):
    """
    Return the index of the max value in actions.
    If there are multiple max, return a random index.

    :param actions: List of actions weights
    """
    maxs = np.argwhere(actions == actions.max()).flatten()

    return np.random.choice(maxs)


def q_learning():
    q = defaultdict(lambda: np.ones(ACTIONS) / ACTIONS)

    position = Position(*INITIAL_POS)

    for t in itertools.count():
        done = False
        for i in range(MAX_ITERATIONS):
            state = position.get_tuple()
            action = get_max_action(q[state])

            position.move(action)
            next_state = position.get_tuple()

            reward = get_reward(next_state)
            tmp = reward + GAMMA * q[next_state].max()
            tmp = tmp - q[state][action]
            q[state][action] += ALPHA * tmp
            
            sys.stdout.write(f'\rT: {t} - {i}/{MAX_ITERATIONS}: Position: {next_state}')
            sys.stdout.flush()


            if reward == 1:
                done = True
                break

        if done:
            break
        else:
            position = Position(*INITIAL_POS)

    return q

if __name__ == "__main__":
    q = q_learning()
    # print(q)
