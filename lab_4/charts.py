import os
import matplotlib.pyplot as plt
import numpy as np


def calc_avg(bests_fitnesses):
    cumsum = np.cumsum(bests_fitnesses)
    for i in range(len(cumsum)):
        cumsum[i] /= i + 1
    return cumsum


def draw_chart(bests_fitnesses, populations, title):
    plt.plot(bests_fitnesses, label='Best so far')
    plt.plot(calc_avg(bests_fitnesses), label='Off-line')
    plt.plot(calc_avg(populations), label='On-line')
    plt.ylabel('Fitness')
    plt.xlabel('Epoch')
    plt.ylim(bottom=0.4, top=1.0)
    plt.xlim(left=0)
    plt.legend()
    plt.title(title)


    os.makedirs('imgs', exist_ok=True)
    plt.savefig('imgs/{}.svg'.format(title.replace(' ', '_')))


