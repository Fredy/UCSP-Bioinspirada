from random import random, randrange, randint


def crossover1(gen1, gen2, point=None):
    if point is None:
        point = randint(0, len(gen1))

    for i in range(point):
        gen1[i], gen2[i] = gen2[i], gen1[i]


def crossover2(gen1, gen2, point1=None, point2=None):
    if point1 is None:
        point1 = randint(0, len(gen1))
    if point2 is None:
        point2 = randint(0, len(gen1))

    if point1 > point2:
        point1, point2 = point2, point1

    for i in range(point1, point2):
        gen1[i], gen2[i] = gen2[i], gen1[i]


def crossover_uniform(gen1, gen2):
    for i in range(len(gen1)):
        if random() >= 0.5:
            gen1[i], gen2[i] = gen2[i], gen1[i]


def mutation(gen):
    rnd = randrange(0, len(gen))
    gen[rnd] = not gen[rnd]


crossovers = dict(
    crossover1=crossover1,
    crossover2=crossover2,
    crossover_uniform=crossover_uniform
)
