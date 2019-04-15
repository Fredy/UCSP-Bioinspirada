import numpy as np
from math import log2
from random import choices


class Cromosome:
    """Represents each of the population individuals"""

    def __init__(self, limits, precisions):
        if len(limits) != len(precisions):
            raise ValueError(
                'len(limits) must equals len(precisions): {} != {}'.format(
                    len(limits), len(precisions)
                )
            )

        self.bin_real_repr = [
            BinRealRepr(lim[0], lim[1], prec)
            for lim, prec in zip(limits, precisions)
        ]
        self.bin_value = []
        self._acc_limits = [0]

        for idx, rep in enumerate(self.bin_real_repr):
            self.bin_value.extend(rep.randomize())
            last = self._acc_limits[-1]
            self._acc_limits.append(last + rep.length)

        self.bin_value = np.array(self.bin_value)

    def get(self, index):
        if index >= len(self.bin_real_repr):
            raise IndexError('Max index is {}'.format(
                len(self.bin_real_repr) - 1))

        start = self._acc_limits[index]
        end = self._acc_limits[index + 1]
        return self.bin_value[start:end]

    def get_real_val(self):
        real_val = []
        for idx, rep in enumerate(self.bin_real_repr):
            real_val.append(rep.get_real_val(self.get(idx)))

        return np.array(real_val)


class BinRealRepr:
    """Binary to Real representation"""

    def __init__(self, left, right, precision):
        self.left = left
        self.right = right
        self.precision = precision
        self.length = round(log2(right - left) + precision * log2(10))

    def randomize(self):
        return choices([False, True], k=self.length)

    def get_real_val(self, bin_value):
        acc = 0
        for i, v in enumerate(bin_value[::-1]):
            acc += 2**i * int(v)
        acc *= (self.right - self.left) / (2 ** self.length - 1)
        return round(self.left + acc, self.precision)
