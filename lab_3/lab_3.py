"""Lab 3: Genetic Algorithms"""
import numpy as np
from math import sin, sqrt, log2


class Repr:
    def __init__(self, number, right, left, precision):
        self.number = number
        self.precision = precision
        self.right = right
        self.left = left
        self.bsize = log2(right - left) + precision * log2(10)

    def real(self):
        round(self.numeber, self.precision)

    def binary(self):
        # self.left + 

        c = 0
        for idx, i in enumerate(s):
            if i == '1':
                c += 2**idx
        


        # right , left
        # precision
        # l_i = log2(right - left) + precision * log2(10)
        # parte entera + parte decimal


def canonical(size, limits, optfunc):
    population = np.random.uniform(limits[0], limits[1], size)
    # TODO: decodificar

    fx = optfunc(population)


def optfunc(x):
    # −100 ≤ x1 ≤ 100
    # −100 ≤ x2 ≤ 100
    xsqr = x[0] ** 2 + x[1] ** 2
    tmp1 = sin(sqrt(xsqr))**2 - 0.5
    tmp2 = (1 + 0.001 * (xsqr)) ** 2
    return 0.5 - tmp1 / tmp2
