"""Lab 3: Genetic Algorithms"""
from random import random, randrange, sample, choice
from sys import argv
from copy import deepcopy
from math import sin, sqrt
import numpy as np
from fitness import calc_fitnesses, linear_normalization
from operators import crossovers, mutation
from selection import selections, elitism
from representation import Cromosome
from charts import draw_chart


def canonical(optfunc, population_len, limits, precisions, epochs,
              crossover_type, selection_type, pc, pm, use_elitism,
              use_normalization, minv=None, maxv=None, save_bests=False, save_pops=False):
    if use_normalization and (minv is None or maxv is None):
        raise TypeError(
            'If use_normalization is true, minv and maxv must be specified'
        )

    bests = [] if save_bests else None
    pops = [] if save_pops else None

    crossover = crossovers[crossover_type]
    selection = selections[selection_type]

    population = np.array([Cromosome(limits, precisions)
                           for i in range(population_len)])
    fitnesses = calc_fitnesses(population, optfunc)

    if use_normalization:
        normalized = linear_normalization(fitnesses, minv, maxv)
        population = population[[i[0] for i in normalized]]
        fitnesses = [i[1] for i in normalized]

    if save_bests:
        idx = np.argmax(fitnesses)
        bests.append(population[idx].get_real_val())
    if save_pops:
        pops.append([c.get_real_val() for c in population])

    for i in range(epochs - 1):
        new_pop = selection(population, fitnesses)
        if use_elitism:
            prev_best = elitism(population, fitnesses)

        operate(new_pop, crossover, pc, pm)

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
            bests.append(population[idx].get_real_val())
        if save_pops:
            pops.append([c.get_real_val() for c in population])

    return population, bests, pops


def operate(population, crossover, pc, pm):
    length = len(population)
    for i in range(length):
        if random() < pc:
            samp = sample(list(population), 2)
            bin_reprs = [i.bin_value for i in samp]
            crossover(bin_reprs[0], bin_reprs[1])
        if random() < pm:
            bin_rep = choice(population).bin_value
            mutation(bin_rep)


def optfunc(x):
    # −100 ≤ x1 ≤ 100
    # −100 ≤ x2 ≤ 100
    xsqr = x[0] ** 2 + x[1] ** 2
    tmp1 = sin(sqrt(xsqr))**2 - 0.5
    tmp2 = (1 + 0.001 * (xsqr)) ** 2
    return 0.5 - tmp1 / tmp2


if __name__ == "__main__":
    if len(argv) < 10:
        print(
            'Usage python lab_3.py population_length epochs experiments crossover selection pc pm use_elitism use_norm',
            '- population_length: length of the population',
            '- epochs: number of epochs',
            '- experiments: number of experiments',
            '- crossover: one of {}'.format(list(crossovers.keys())),
            '- selection: one of {}'.format(list(selections.keys())),
            '- pc: cross probability',
            '- pm: mutation probaility',
            '- use_elitism: true or false',
            '- use_norm: true or false',
            '- if use_norm is true: two extra params must be specified: vmin and vmax',
            sep='\n'
        )
        exit()

    population_len = int(argv[1])
    epochs = int(argv[2])
    experiments = int(argv[3])
    crossover = argv[4]
    selection = argv[5]
    pc = float(argv[6])
    pm = float(argv[7])
    use_elitism = argv[8] == 'true'
    use_norm = argv[9] == 'true'

    if use_norm:
        if len(argv) < 12:
            print('If use_norm is true: two extra params must be specified: minv and maxv')
            exit()
        minv = float(argv[10])
        maxv = float(argv[11])

    bests_fitnesses = np.zeros(epochs)
    population_fitnesses = np.zeros(epochs)
    for i in range(experiments):
        res, bests, pops = canonical(
            optfunc=optfunc, population_len=population_len,
            limits=((-100, 100), (-100, 100)),
            precisions=(6, 6), epochs=epochs,
            crossover_type=crossover,
            selection_type=selection, pc=pc, pm=pc,
            use_elitism=use_elitism, use_normalization=use_norm,
            minv=minv, maxv=maxv,
            save_bests=True,
            save_pops=True
        )

        fitnesses = calc_fitnesses(bests, optfunc)
        bests_fitnesses += fitnesses

        population_f = []
        for i in pops:
            tmp = np.average(calc_fitnesses(i, optfunc))
            population_f.append(tmp)

        population_fitnesses += population_f

        res_fit = calc_fitnesses(res, optfunc)
        for r, f in  zip(res, res_fit):
            print(r.get_real_val(), ' : ', f)
        print('------')

    bests_fitnesses /= experiments
    population_fitnesses /= experiments

    draw_chart(bests_fitnesses, population_fitnesses, '{} {} pc: {} pm: {} E: {} N: {}'.format(
        selection, crossover, pc, pm, use_elitism, use_norm))

    res_fitnesses = calc_fitnesses(res, optfunc)
    best_idx = np.argmax(res_fitnesses)
    print(res[best_idx].get_real_val(), '  -> ', res_fitnesses[best_idx])

    print(bests_fitnesses)
