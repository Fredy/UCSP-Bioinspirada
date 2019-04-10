"""Lab 3: Genetic Algorithms"""
import numpy as np
from math import sin, sqrt, log2
from random import choices, randrange, random

#pupulation = [ value, ... ]
# fitness = [f0, ..., fn]

# Representation


class BinRealRepr:
    """Binary to Real representation"""

    def __init__(self, left, right, precision):
        self.left = left
        self.right = right
        self.precision = precision
        self.length = round(log2(right - left) + precision * log2(10))

    def randomize(self):
        self.bin_value = choices(['0', '1'], k=self.length)

    def get_real_val(self):
        acc = 0
        for i, v in enumerate(self.bin_value[::-1]):
            acc += 2**i * int(v)
        acc *= (self.right - self.left) / (2 ** self.length - 1)
        return round(self.left + acc, self.precision)

# Selection


def roulette(population, fitnesses, offspring_len=None):
    if offspring_len is None:
        offspring_len = len(population)
    return choices(population, weights=fitnesses, k=offspring_len)


def stochastic(population, fitnesses, offspring_len=None):
    if offspring_len is None:
        offspring_len = len(population)

    tmp = len(population) / sum(population)
    values = [tmp * i for i in fitnesses]
    int_part = [int(i) for i in values]
    dec_part = [i - j for i, j in zip(values, int_part)]

    res = []
    for i, v in enumerate(int_part):
        res.extend([population[i]] * v)

    remm = offspring_len - len(res)
    res.extend(roulette(population, dec_part, remm))

    return res


def tournament(population, fitnesses, offspring_len=None):
    if offspring_len is None:
        offspring_len = len(population)

    zipped = list(zip(population, fitnesses))

    res = []
    for i in range(offspring_len):
        tmp = choices(zipped, k=2)
        res.append(tmp[0] if tmp[0] > tmp[1] else tmp[1])


# Adjust

def linear_normalization(fitnesses, minv, maxv):
    """
    :return: list of tuples (idx in population, new fitness)
    """
    enumerated = list(enumerate(fitnesses))
    enumerated.sort(key=lambda x: x[1])

    tmp = (maxv - minv) / (len(fitnesses) - 1)
    return [
        (v[0], minv + tmp * (idx - 1))
        for idx, v in enumerate(enumerated, start=1)
    ]

# Operators

def crossover1(gen1,gen2, length, point=None):
    if point is None:
        point = randrange(0, length)
    return (
        gen1[:point] + gen2[point:],
        gen2[:point] + gen1[point:]
    )

def crossover2(gen1,gen2, length, point1=None, point2=None):
    if point1 is None:
        point1 = randrange(0, length)
    if point2 is None:
        point2 = randrange(0, length)

    if point1 > point2:
        point1, point2 = point2, point1 
    
    return (
    gen1[:point1] + gen2[point1:point2] + gen1[point2:],
    gen2[:point1] + gen1[point1:point2] + gen2[point2:]
    )

def crossover_uniform(gen1,gen2, length):
    new_gen1 = []
    new_gen2 = []
    for i in range(length):
        if randon() >= 0.5:
            new_gen1.append(gen2[i])
            new_gen2.append(gen1[i])
        else:
            new_gen1.append(gen1[i])
            new_gen2.append(gen2[i])

    return (new_gen1, new_gen2)


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
