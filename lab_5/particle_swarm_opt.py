import os
import sys
import csv
from copy import deepcopy
from math import gamma, pi, sin

import numpy as np

DIMENSIONS = 2
TRIALS = 20
POPULATION_SIZE = 50
ITERATIONS = 50

OMEGA = 0.5
PHI_P = 0.75
PHI_G = 0.25


class Individual:
    def __init__(self, func):
        min_ = func.min_domain
        max_ = func.max_domain
        vmax = abs(max_ - min_)
        vmin = -vmax

        self.position = np.random.rand(DIMENSIONS) * (max_ - min_) + min_
        self.velocity = np.random.rand(DIMENSIONS) * (vmax - vmin) + vmin

        self.personal_best = self.position.copy()

        self.fitness = func(self.position)
        self._func = func

    def update_velocity(self, best_pos):
        rp = np.random.uniform(1, -1,size=DIMENSIONS)
        rg = np.random.uniform(1, -1,size=DIMENSIONS)
        tmp_p = PHI_P * rp * (self.personal_best - self.position)
        tmp_g = PHI_G * rg * (best_pos - self.position)
        self.velocity = OMEGA * self.velocity + tmp_p + tmp_g

    def update_position(self):
        self.position += self.velocity

        # Correct bound violations
        for i in range(DIMENSIONS):
            if self.position[i] > self._func.max_domain:
                self.position[i] = self._func.max_domain
            elif self.position[i] < self._func.min_domain:
                self.position[i] = self._func.min_domain

        new_fitness = self._func(self.position)

        # Updates personal best
        if self._func.optim_oper(new_fitness, self.fitness):
            self.fitness = new_fitness
            self.personal_best = self.position.copy()

    def copy(self):
        return deepcopy(self)


def particle_swarm_opt(func, trials=TRIALS, verbose=True):
    # CSV output
    os.makedirs('results', exist_ok=True)
    out_file_name = os.path.join('results', 'results_pso.csv')

    results = open(out_file_name, 'w+')
    results_writer = csv.writer(results, lineterminator="\n")

    for trial in range(trials):
        # Just for test puposes
        # np.random.seed(2)

        # Fitness list
        fitnesses = []
        # Initial population
        individuals = [Individual(func) for i in range(POPULATION_SIZE)]
        individuals.sort(key=lambda x: x.fitness, reverse=func.isMax)

        # Initial best
        best = individuals[0].copy()

        for iteration in range(ITERATIONS):
            for ind in individuals[1:]:
                # Update velocities and positions.
                ind.update_velocity(best.position)
                ind.update_position()

            # Update best global
            individuals.sort(key=lambda x: x.fitness, reverse=func.isMax)

            if func.optim_oper(individuals[0].fitness, best.fitness):
                best = individuals[0].copy()

            if verbose:
                sys.stdout.write(
                    f'\rTrial: {trial:4}, Iteration: {iteration:4}, '
                    f'Best Fitness: {best.fitness:.4f}'
                )

            fitnesses.append(best.fitness)

        results_writer.writerow(fitnesses)

    results.close()
