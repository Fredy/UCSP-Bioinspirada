from copy import deepcopy
from random import choices
import numpy as np


def roulette(population, fitnesses, offspring_len=None):
    if offspring_len is None:
        offspring_len = len(population)
    res = choices(population, weights=fitnesses, k=offspring_len)

    return np.array([deepcopy(i) for i in res])


def stochastic(population, fitnesses, offspring_len=None):
    if offspring_len is None:
        offspring_len = len(population)

    tmp = len(fitnesses) / sum(fitnesses)
    values = [tmp * i for i in fitnesses]
    int_part = [int(i) for i in values]
    dec_part = [i - j for i, j in zip(values, int_part)]

    res = []
    for i, v in enumerate(int_part):
        res.extend([population[i]] * v)

    remm = offspring_len - len(res)
    res.extend(roulette(population, dec_part, remm))

    return np.array([deepcopy(i) for i in res])


def tournament(population, fitnesses, offspring_len=None):
    if offspring_len is None:
        offspring_len = len(population)

    zipped = list(zip(population, fitnesses))

    res = []
    for i in range(offspring_len):
        tmp = choices(zipped, k=2)
        res.append(tmp[0][0] if tmp[0][1] > tmp[1][1] else tmp[1][0])

    return np.array([deepcopy(i) for i in res])

def elitism(population, fitnesses):
    idx = np.argmax(fitnesses)
    return (population[idx], fitnesses[idx])


selections = dict(
    roulette=roulette,
    stochastic=stochastic,
    tournament=tournament
)
