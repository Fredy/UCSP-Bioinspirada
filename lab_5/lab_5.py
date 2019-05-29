import numpy as np
from math import sin, sqrt

# Benchmarks

def schwefel(x):
    # Domain:
    #  x_i ∈ [−500, 500]
    # Global minimum:
    #  f_2(x°) = 0, x° = (420,9687,...,420,9687)
    res = 418.9829 * len(x)

    for i in x:
        res -= i * sin(sqrt(abs(i)))

    return res


def function_3(x):
    # Domain:
    #  −100 ≤ xi ≤ 100
    # Global maximum:
    #  f_3(x°) = 1, x° = {0,0,...,0)
    square_res = 0
    for i in x:
        square_res += x**2

    sin_res = sin(square_res)

    return 0.5 - (sin_res**2 - 0.5) / (1.0 + 0.001 * square_res) ** 2

# Cukoo
# PSO
