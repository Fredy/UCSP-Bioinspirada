import numpy as np
from random import random, randrange, sample, choice
from math import sin, sqrt
from sys import argv
from copy import deepcopy

from fitness import linear_normalization, calc_fitnesses
from selection import selections, elitism
from charts import draw_chart
from operators import mutations, crossovers
from representation import Cromosome


def canonical(optfunc, population_len, limits, epochs,
              crossover_type, selection_type, mutation_type,
              pc, pm, use_elitism, use_normalization, minv=None, maxv=None,
              save_bests=False, save_pops=False):
    if use_normalization and (minv is None or maxv is None):
        raise TypeError(
            'If use_normalization is true, minv and maxv must be specified'
        )

    bests = [] if save_bests else None
    pops = [] if save_pops else None

    crossover = crossovers[crossover_type]
    selection = selections[selection_type]
    mutation = mutations[mutation_type]

    population = np.array([Cromosome(limits)
                           for i in range(population_len)])
    fitnesses = calc_fitnesses(population, optfunc)

    if use_normalization:
        normalized = linear_normalization(fitnesses, minv, maxv)
        population = population[[i[0] for i in normalized]]
        fitnesses = [i[1] for i in normalized]

    if save_bests:
        idx = np.argmax(fitnesses)
        bests.append(population[idx])
    if save_pops:
        pops.append(population)

    for i in range(epochs - 1):
        new_pop = selection(population, fitnesses)
        if use_elitism:
            prev_best = elitism(population, fitnesses)

        operate(new_pop, crossover, mutation, pc, pm, i, epochs, 1)

        fitnesses = calc_fitnesses(new_pop, optfunc)

        if use_elitism:
            idx = randrange(len(new_pop))
            new_pop[idx] = deepcopy(prev_best[0])
            fitnesses[idx] = prev_best[1]

        if use_normalization:
            normalized = linear_normalization(fitnesses, minv, maxv)
            population = deepcopy(new_pop[[i[0] for i in normalized]])
            fitnesses = [i[1] for i in normalized]
        else:
            population = new_pop

        if save_bests:
            idx = np.argmax(fitnesses)
            bests.append(population[idx])
        if save_pops:
            pops.append(population)

    return population, bests, pops


def operate(population, crossover, mutation, pc, pm, epoch, max_epoch, beta):
    length = len(population)
    for i in range(length):
        if random() < pc:
            samp = sample(population.tolist(), 2)
            crossover(samp[0], samp[1])
        if random() < pm:
            tmp = choice(population)
            mutation(tmp, epoch, max_epoch, beta)


def optfunc(x, dimension):
    # −100 ≤ x1 ≤ 100
    # −100 ≤ x2 ≤ 100

    sqr_sum = (x ** 2).sum()
    numerator = sin(sqrt(sqr_sum)) ** 2 - 0.5
    denominator = (1 + 0.0001 * sqr_sum) ** 2
    return 0.5 - numerator/denominator


if __name__ == "__main__":
    if len(argv) < 11:
        print(
            'Usage python lab_3.py population_length epochs experiments crossover selection pc pm use_elitism use_norm',
            '- bencmark_func_dim: dimension of the benchmark function',
            '- population_length: length of the population',
            '- epochs: number of epochs',
            '- experiments: number of experiments',
            '- crossover: one of {}'.format(list(crossovers.keys())),
            '- mutation: one of {}'.format(list(mutations.keys())),
            '- selection: one of {}'.format(list(selections.keys())),
            '- pc: cross probability',
            '- pm: mutation probaility',
            '- use_elitism: true or false',
            '- use_norm: true or false',
            '- if use_norm is true: two extra params must be specified: vmin and vmax',
            sep='\n'
        )
        exit()

    benchmark_func_dim = int(argv[1])
    population_len = int(argv[2])
    epochs = int(argv[3])
    experiments = int(argv[4])
    crossover = argv[5]
    mutation = argv[6]
    selection = argv[7]
    pc = float(argv[8])
    pm = float(argv[9])
    use_elitism = argv[10] == 'true'
    use_norm = argv[11] == 'true'

    minv = None
    maxv = None
    if use_norm:
        if len(argv) < 14:
            print(
                'If use_norm is true: two extra params must be specified: minv and maxv')
            exit()
        minv = float(argv[12])
        maxv = float(argv[13])

    def _optfunc(x):
        return optfunc(x, benchmark_func_dim)

    bests_fitnesses = np.zeros(epochs)
    population_fitnesses = np.zeros(epochs)
    for i in range(experiments):
        res, bests, pops = canonical(
            optfunc=_optfunc,
            population_len=population_len,
            limits=((-100, 100),) * benchmark_func_dim,
            epochs=epochs,
            crossover_type=crossover,
            mutation_type=mutation,
            selection_type=selection,
            pc=pc, pm=pm,
            use_elitism=use_elitism, use_normalization=use_norm,
            minv=minv, maxv=maxv,
            save_bests=True,
            save_pops=True
        )

        fitnesses = calc_fitnesses(bests, _optfunc)
        bests_fitnesses += fitnesses

        population_f = []
        for i in pops:
            tmp = np.average(calc_fitnesses(i, _optfunc))
            population_f.append(tmp)

        population_fitnesses += population_f

        res_fit = calc_fitnesses(res, _optfunc)
        # for r, f in zip(res, res_fit):
        #     print(r.values, ' : ', f)
        # print('------')

    bests_fitnesses /= experiments
    population_fitnesses /= experiments

    draw_chart(bests_fitnesses, population_fitnesses, '{} {} pc: {} pm: {} E: {} N: {} D: {}'.format(
        crossover, mutation, pc, pm, use_elitism, use_norm, benchmark_func_dim))

    res_fitnesses = calc_fitnesses(res, _optfunc)
    best_idx = np.argmax(res_fitnesses)
    print(res[best_idx].values, '  -> ', res_fitnesses[best_idx])
