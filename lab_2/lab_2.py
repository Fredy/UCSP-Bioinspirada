from numpy import random

# 1.
def evo_strategy(opt_f, size, max_gen, variance,k, c):
    x = random.uniform(-2.048, 2.048, size)
    fx = opt_f(x)
    p = 0
    for i in range(max_gen):
        x += random.normal(scale=variance)
        new_fx = opt_f(x)

        if new_fx > fx:
            fx = new_fx
            p += 1

        print(i, ':', x, '=>', fx)

        if i % k == 0:
            tmp = p/k
            if tmp < 0.2:
                variance /= c
            elif tmp > 0.2:
                variance *= c

# (μ + 1)-EE, combinación lineal convexa

def func_1(x):
    # -2.048 <= x1 < 2.048
    # -2.048 <= x2 < 2.048
    return 100 * (x[0] ** 2 - x[1] ** 2) + (1 - x[0]) ** 2


if __name__ == '__main__':
    evo_strategy(func_1, 2, 40, 3, 10, 0.817)
