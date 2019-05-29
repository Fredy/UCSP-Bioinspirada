import numpy as np


class Cromosome:
    """Represents each of the population individuals"""
    def __init__(self, limits):
        self.limits = limits
        self.values = np.random.rand(len(limits))
        for idx, (left, right) in enumerate(limits):
            self.values[idx] *= (right - left) + left
    
    def __len__(self):
        return len(self.limits)
