from collections.abc import Iterable


def linear_normalization(fitnesses, minv, maxv):
    """
    :return: list of tuples (idx in population, new fitness)
    """
    enumerated = list(enumerate(fitnesses))
    enumerated.sort(key=lambda x: x[1])

    tmp = (maxv - minv) / (len(fitnesses) - 1)
    return [
        (v[0], minv + tmp * (idx - 1))
        for idx, v in enumerate(enumerated, start=1)
    ]


def calc_fitnesses(population, evalfunc):
    return [evalfunc(i.values) for i in population]
