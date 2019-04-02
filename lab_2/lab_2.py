from numpy import random
from random import choice

# 1.


def evo_strategy(opt_f, mutate, size, limits, max_gen, sigma, k, c):
    x = random.uniform(limits[0], limits[1], size)
    fx = opt_f(x)
    p = 0
    print('- :', x, '=>', fx)
    for i in range(max_gen):
        new_x = mutate(x, 0, sigma, limits)
        new_fx = opt_f(new_x)

        if new_fx > fx:
            fx = new_fx
            x = new_x
            p += 1
            print(i, ':', x, '=>', fx)

        if i % k == 0:
            tmp = p/k
            if tmp < 0.2:
                sigma /= c
            elif tmp > 0.2:
                sigma *= c


def mutate(x, mean, stdev, limits):
    while True:
        rnd = random.normal(loc=mean, scale=stdev, size=x.size)
        new_x = x + rnd
        if all(limits[0] <= i < limits[1] for i in new_x):
            return new_x

# 2
#  (μ + 1)-EE, combinación lineal convexa


def evo_strategy_plus(opt_f, mutate, mu, lambd, size, limits,
                      max_gen, sigma, k, c):
    x = [
        random.uniform(limits[0], limits[1], size)
        for i in range(mu)
    ]
    x = [dict(y=opt_f(i), s=i) for i in x]

    for i in range(max_gen):
        print(i, '---------', sigma)
        for pop in x:
            print('   ', pop['s'], '->', pop['y'])
        offspring = gen_offspring(
            parents=x,
            size=lambd,
            opt_f=opt_f,
            mutate=mutate,
            mean=0,
            stdev=sigma,
            limits=limits
        )

        x.extend(offspring)
        x = selection(x, mu)

def evo_strategy_comma(opt_f, mutate, mu, lambd, size, limits,
                      max_gen, sigma, k, c):
    x = [
        random.uniform(limits[0], limits[1], size)
        for i in range(mu)
    ]
    x = [dict(y=opt_f(i), s=i) for i in x]

    for i in range(max_gen):
        print(i, '---------', sigma)
        for pop in x:
            print('   ', pop['s'], '->', pop['y'])
        offspring = gen_offspring(
            parents=x,
            size=lambd,
            opt_f=opt_f,
            mutate=mutate,
            mean=0,
            stdev=sigma,
            limits=limits
        )

        x = selection(offspring, mu)

def gen_offspring(parents, size, opt_f, mutate, mean, stdev, limits):
    offspring = []
    for i in range(size):
        parent = choice(parents)
        child = mutate(parent['s'], mean, stdev, limits)
        fx = opt_f(child)
        offspring.append(dict(y=fx, s=child))

    return offspring

def selection(population, size):
    population.sort(key=lambda x: x['y'], reverse=True)

    return population[:size]


def func_1(x):
    # -2.048 <= x1 < 2.048
    # -2.048 <= x2 < 2.048
    return 100 * (x[0] ** 2 - x[1] ** 2) + (1 - x[0]) ** 2


if __name__ == '__main__':
    # evo_strategy(
    #     opt_f=func_1,
    #     mutate=mutate,
    #     size=2,
    #     limits=(-2.048, 2.048),
    #     max_gen=40,
    #     sigma=3,
    #     k=10,
    #     c=0.817
    # )

    evo_strategy_comma(
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