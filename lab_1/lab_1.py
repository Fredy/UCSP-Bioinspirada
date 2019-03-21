from random import random
from math import log2

def gen_random_list(n):
    ran = [random() for i in range(n)]

    return list(map(lambda x: x/ sum(ran), ran))

# 1. Hartley, Shannon
def hartley(probs):
    return log2(len(probs))

def shannon(probs):
    count = 0
    for i in probs:
        count += i * log2(i)
    return - count

# 2.

def frequency(file_name):
    with open(file_name) as file:
        counts = {}
        for line in file:
            for char in line.lower():
                if not (char.isalpha() or char == ' '):
                    continue
                if char in counts:
                    counts[char] += 1
                else:
                    counts[char] = 1

    
    csum = 0    
    for key in counts:
        csum += counts[key]
     
    letters = []
    for key, val in sorted(counts.items()):
        letters.append((key,val / csum))

    return letters

def text_entropy(file_name_list):
    for name in file_name_list:
        freq = frequency(name)
        freq_val = [v for _, v in freq]
        print('----{}----'.format(name))
        print('Hartley:', round(hartley(freq_val),4))
        print('Shannon:', round(shannon(freq_val),4))



if __name__ == '__main__':
    text_entropy(['text_1.txt', 'text_2.txt', 'text_3.txt'])
    # ----text_1.txt----
    # Hartley: 4.9542
    # Shannon: 4.0948
    # ----text_2.txt----
    # Hartley: 5.0444
    # Shannon: 4.1074
    # ----text_3.txt----
    # Hartley: 5.0
    # Shannon: 4.123 
    # + Los textos tienen la misma entropía de Hartley, porque
    #   el total  de elementos alfabeto usado es el mismo:
    #   letras en español + letras con acentos + espacio (27 + 5 + 1)
    # + La entropía de Shannon es similar en todos porque todos los textos están
    #   escritos en español