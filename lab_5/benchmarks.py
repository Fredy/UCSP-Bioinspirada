# Benchmarks
from math import sin, sqrt
import operator


class Benchmark:
    def __init__(self, func, min_, max_, optim_oper):
        self.func = func
        self.min_domain = min_
        self.max_domain = max_
        self.optim_oper = optim_oper
        self.isMax = optim_oper is operator.gt

    def __call__(self, x):
        return self.func(x)


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
        square_res += i**2

    sin_res = sin(sqrt(square_res))

    return 0.5 - (sin_res**2 - 0.5) / ((1.0 + 0.001 * square_res) ** 2)


def aeckley(x):
    # Domain:
    # −32.768 ≤ x ≤ 32.768
    #  aeckley(x°) = 1, x° = {0,0,...,0)
    pass


schwefel = Benchmark(schwefel, -500, 500, operator.lt)
function_3 = Benchmark(function_3, -100, 100, operator.gt)
# TODO: make decorator and replace the above two lines
