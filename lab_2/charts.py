from lab_2 import (evo_strategy, evo_strategy_comma,
                   evo_strategy_plus, func_1, mutate)

import matplotlib.pyplot as plot
import numpy as np


def get_best_fitness(result):
    bests = []
    for i in result:
        if isinstance(i, list):
            bests.append(i[0]['y'])
        else:
            bests.append(i['y'])

    return bests


def get_bassic_fitness(iterations):
    res = np.zeros((1, 40))
    for i in range(iterations):
        basic = evo_strategy(
            opt_f=func_1,
            mutate=mutate,
            size=2,
            limits=(-2.048, 2.048),
            max_gen=40,
            sigma=3,
            k=10,
            c=0.817
        )

        res += get_best_fitness(basic)

    res /= 20
    return res.tolist()[0]


def get_comma_fitness(iterations):
    res = np.zeros((1, 40))
    for i in range(iterations):
        comma = evo_strategy_comma(
            mu=5,
            lambd=10,
            opt_f=func_1,
            mutate=mutate,
            size=2,
            limits=(-2.048, 2.048),
            max_gen=40,
            sigma=3,
            k=10,
            c=0.817

        )

        res += get_best_fitness(comma)

    res /= 20
    return res.tolist()[0]


def get_plus_fitness(iterations):
    res = np.zeros((1, 40))
    for i in range(iterations):
        plus = evo_strategy_plus(
            mu=5,
            lambd=10,
            opt_f=func_1,
            mutate=mutate,
            size=2,
            limits=(-2.048, 2.048),
            max_gen=40,
            sigma=3,
            k=10,
            c=0.817

        )

        res += get_best_fitness(plus)

    res /= 20
    return res.tolist()[0]


if __name__ == "__main__":

    plot.plot(get_bassic_fitness(20), label='(1 + 1)-EE')
    plot.plot(get_plus_fitness(20), label='(μ + λ)−EE,')
    plot.plot(get_comma_fitness(20), label='(μ, λ)−EE,')
    plot.ylabel('Fitness')
    plot.xlabel('Iteration')
    plot.legend()
    plot.savefig('comparison.svg')
