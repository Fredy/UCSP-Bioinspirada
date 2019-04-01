from numpy import random

# 1.


def evo_strategy(opt_f, size, limits, max_gen, sigma, k, c):
    x = random.uniform(limits[0], limits[1], size)
    fx = opt_f(x)
    p = 0
    for i in range(max_gen):
        x = mutate(x, 0, sigma, limits)
        new_fx = opt_f(x)

        if new_fx > fx:
            fx = new_fx
            p += 1

        print(i, ':', x, '=>', fx)

        if i % k == 0:
            tmp = p/k
            if tmp < 0.2:
                sigma /= c
            elif tmp > 0.2:
                sigma *= c


def mutate(x, mu, sigma, limits):
    rnd = random.normal(loc=mu, scale=sigma, size=x.size)
    new_x = x + rnd
    while not (all(limits[0] <= i < limits[1] for i in new_x)):
        rnd = random.normal(loc=mu, scale=sigma, size=x.size)
        new_x = x + rnd

    return new_x


# (μ + 1)-EE, combinación lineal convexa

def func_1(x):
    # -2.048 <= x1 < 2.048
    # -2.048 <= x2 < 2.048
    return 100 * (x[0] ** 2 - x[1] ** 2) + (1 - x[0]) ** 2


if __name__ == '__main__':
    evo_strategy(opt_f=func_1, size=2, limits=(-2.048, 2.048),
                 max_gen=400, sigma=3, k=10, c=0.817)
