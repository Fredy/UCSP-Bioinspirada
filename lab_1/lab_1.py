from random import (random, choices)
from math import log2
from collections import (Counter, OrderedDict)
from string import ascii_lowercase

ALPHABET = ascii_lowercase + 'ñáéíóú '


def gen_random_list(n):
    ran = [random() for i in range(n)]

    return list(map(lambda x: x / sum(ran), ran))

# 1. Hartley, Shannon


def hartley(probs):
    return log2(len(probs))


def shannon(probs):
    count = 0
    for i in probs:
        if i == 0:
            continue
        count += i * log2(i)
    return - count

# 2. 3.


def frequency(file_name):
    with open(file_name) as file:
        counts = Counter(char for line in file
                         for char in line.lower()
                         if char in ALPHABET
                         )

    csum = sum(counts.values())

    letters = {i: 0 for i in ALPHABET}
    for key, val in counts.items():
        letters[key] = val / csum

    return letters


def text_entropy(file_name_list):
    for name in file_name_list:
        freq = frequency(name)
        freq_val = freq.values()
        print('----{}----'.format(name))
        print('Hartley:', round(hartley(freq_val), 4))
        print('Shannon:', round(shannon(freq_val), 4))

# 4.


def gen_random_text_1(file_name, size):
    '''Completely random text generator'''
    chars = choices(ALPHABET, k=size)

    with open(file_name, 'w') as file:
        file.write(''.join(chars))


def gen_random_text_2(file_name, weights, size):
    '''Random text generator using weights'''
    chars = choices(ALPHABET, weights=weights, k=size)

    with open(file_name, 'w') as file:
        file.write(''.join(chars))


if __name__ == '__main__':
    text_entropy(['text_1.txt', 'text_2.txt', 'text_3.txt'])

    print('\nLipograms:')
    text_entropy(['lipogram_1.txt', 'lipogram_2.txt'])

    gen_random_text_1('random_no_w.txt', 4000)

    freq = frequency('text_2.txt')

    weights = [freq[i] for i in ALPHABET]

    gen_random_text_2('random_w.txt', weights, 4000)

    print('\nRandoms:')
    text_entropy(['random_no_w.txt', 'random_w.txt'])
