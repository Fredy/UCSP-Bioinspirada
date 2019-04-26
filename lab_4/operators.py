import numpy as np


def uniform_mutation(gen, *args):
    rnd_idx = np.random.randint(len(gen))
    rnd_val = np.random.rand()
    left, right = gen.limits[rnd_idx]

    rnd_val *= (left - right) + left
    gen.values[rnd_idx] = rnd_val


def frontier_mutation(gen, *args):
    rnd = np.random.rand()
    rnd_idx = np.random.randint(len(gen))
    left, right = gen.limits[rnd_idx]

    if rnd < 0.5:
        gen.values[rnd_idx] = left
    else:
        gen.values[rnd_idx] = right


def _non_uni_op(t, y, max_epoch, beta, *args):
    rnd = np.random.rand()
    return y * rnd * (1 - t/max_epoch) ** beta


def non_uniform_mutation(gen, epoch, max_epoch, beta, *args):
    rnd = np.random.rand()
    rnd_idx = np.random.randint(len(gen))
    left, right = gen.limits[rnd_idx]
    val = gen.values[rnd_idx]
    if rnd < 0.5:
        operand = _non_uni_op(epoch, right - val, max_epoch, beta)
    else:
        operand = - _non_uni_op(epoch, val - left, max_epoch, beta)

    gen.values[rnd_idx] += operand


def arith_crossover(gen1, gen2, *args):
    rnd = np.random.rand()

    new1 = rnd * gen1.values + (1-rnd) * gen2.values
    new2 = (1-rnd) * gen1.values + rnd * gen2.values

    gen1.values = new1
    gen2.values = new2


def simple_crossover(gen1, gen2, *args):
    point = np.random.randint(len(gen1))

    for i in range(point):
        gen1.values[i], gen2.values[i] = gen2.values[i], gen1.values[i]


def heuristic_crossover(gen1, gen2, max_iter=100, *args):
    # f_eval(gen2) must be better than f_eval(gen1)

    count = 0
    while True:
        rnd = np.random.rand()
        res = rnd * (gen2.values - gen1.values) + gen2.values

        if all(
            l <= val <= r
            for (r, l), val in zip(gen1.limits, res)
        ):
            return res

        count += 1
        if max_iter is not None and count >= max_iter:
            return None


crossovers = dict(
    arith_crossover=arith_crossover,
    simple_crossover=simple_crossover,
    heuristic_crossover=heuristic_crossover
)

mutations = dict(
    uniform_mutation=uniform_mutation,
    frontier_mutation=frontier_mutation,
    non_uniform_mutation=non_uniform_mutation
)