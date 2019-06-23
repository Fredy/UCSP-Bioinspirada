import numpy as np
import q_learning as ql
from multiprocessing import Pool
import itertools


def test_combinations():
    """Test combinations of α and γ"""
    learning_rate = np.arange(0, 1.1, 0.1)
    dis_factor = np.arange(0, 1.1, 0.1)

    for lr in learning_rate:
        for df in dis_factor:
            ql.ALPHA = lr
            ql.GAMMA = df
            with Pool() as pool:
                res = pool.map(ql.q_learning, itertools.repeat(None, 20))
            avg_iterations = np.mean([i[1] for i in res])

            print(f'| {lr:4} | {df:4} | {round(avg_iterations,2):9} |')


def test_grid_size():
    sizes = [(10, 10), (20, 20), (30, 30), (40, 40), (50, 50),
             (60, 60), (70, 70), (80, 80), (90, 90), (100, 100)]

    for i in sizes:
        ql.GRID_END = i
        ql.R_END, ql.C_END = i
        ql.INITIAL_POS = (ql.R_END//2, ql.C_END//2)
        ql.REWARD_POS = i
        with Pool() as pool:
            res = pool.map(ql.q_learning, itertools.repeat(None, 20))
        avg_iterations = np.mean([i[1] for i in res])

        print(f'| {i[0]}x{i[1]} | {round(avg_iterations, 2):9} |')


if __name__ == "__main__":
    # q, total_iterations = q_learning()
    # print(total_iterations)
    # test_combinations()
    test_grid_size()
