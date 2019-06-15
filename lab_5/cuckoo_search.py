import os
import sys
import csv
from copy import deepcopy
from math import gamma, pi, sin

import numpy as np


LAMBDA = 1.5
STEP_SIZE = 0.01
ABANDON_PROB = 0.25

POPULATION_SIZE = 50
DIMENSIONS = 2
TRIALS = 20
ITERATIONS = 50






def levy_flight(lambda_=LAMBDA):
    """Generates random step length is drawn from a Lévy distribution"""

    tmp = gamma(1 + lambda_) * sin(pi * lambda_ / 2) / \
        gamma(0.5 + lambda_ / 2) * 2 ** (lambda_ / 2 - 0.5)

    sigmax = tmp ** (1 / lambda_)

    u = np.random.normal(0, sigmax, DIMENSIONS)
    v = np.random.normal(0, 1, DIMENSIONS)

    return u / np.fabs(v) ** (1 / lambda_)


class Individual:
    def __init__(self, func):
        self.position = np.random.rand(DIMENSIONS)
        self.position *= (func.max_domain - func.min_domain) + func.min_domain
        self.fitness = func(self.position)
        self._func = func

    def __repr__(self):
        return (f'ID: {id(self)}\n'
                f'+ Fitness: {self.fitness.round(4)}\n'
                f'+ Position: {self.position.round(4)}')

    def abandon(self):
        _min = self._func.min_domain
        _max = self._func.max_domain
        for i in range(DIMENSIONS):
            p = np.random.rand()
            if p < ABANDON_PROB:
                self.position[i] = np.random.rand()
                self.position[i] *= (_max - _min) + _min

        self.fitness = self._func(self.position)

    def update_position(self):
        step = STEP_SIZE * levy_flight()
        self.position += step

        # Correct bound violations
        for i in range(DIMENSIONS):
            if self.position[i] > self._func.max_domain:
                self.position[i] = self._func.max_domain
            elif self.position[i] < self._func.min_domain:
                self.position[i] = self._func.min_domain

        self.fitness = self._func(self.position)

    def copy(self):
        return deepcopy(self)


def cuckoo_search(func, trials=TRIALS, out_file='results_cs.csv', verbose=True):
    # CSV output
    os.makedirs('results', exist_ok=True)
    out_file_name = os.path.join('results', out_file)

    results = open(out_file_name, 'w+')
    results_writer = csv.writer(results, lineterminator="\n")

    for trial in range(trials):
        # Just for test puposes
        # np.random.seed(trial)

        # Fitness list
        fitnesses = []
        # Initial population
        individuals = [Individual(func) for i in range(POPULATION_SIZE)]
        individuals.sort(key=lambda x: x.fitness)

        # Initial best
        best = individuals[0].copy()

        # Main loop
        for iteration in range(ITERATIONS):

            # Generate new solutions
            for ind in individuals:
                ind.update_position()

                # Randomly choose one individual
                rnd = np.random.choice(individuals)
                # Choose a individual that is diferent that actual
                while rnd is ind:
                    rnd = np.random.choice(individuals)

                if func.optim_oper(ind.fitness, rnd.fitness):
                    rnd.position = ind.position.copy()
                    rnd.fitness = ind.fitness

            individuals.sort(key=lambda x: x.fitness)

            # Abandon solutions, keep the best
            for i in range(1, POPULATION_SIZE):
                r = np.random.rand()
                if r < ABANDON_PROB:
                    individuals[i].abandon()

            individuals.sort(key=lambda x: x.fitness)

            if func.optim_oper(individuals[0].fitness, best.fitness):
                best = individuals[0].copy()

            if verbose:
                sys.stdout.write(
                    f'\rTrial: {trial:4}, Iteration: {iteration:4}, '
                    f'Best Fitness: {best.fitness:.4f}'
                )
            # for i in individuals:
            #     # print(f'{i.fitness:.4}', end=', ')
            #     print(i.position)
            # print('--------------')

            fitnesses.append(best.fitness)

        results_writer.writerow(fitnesses)
