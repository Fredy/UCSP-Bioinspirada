import pandas as pd
import benchmarks as bm
import cuckoo_search as cs
import particle_swarm_opt as pso
from scipy.stats import ranksums


def cs_tune(opt_func):
    lambda_ = [1.1, 1.5, 2, 2.5, 3]
    step_size = [0.01, 0.5, 1]

    print('|  λ  |  α   | Resultado |')
    print('|-----|------|-----------|')
    for l in lambda_:
        cs.LAMBDA = l
        for s in step_size:
            cs.STEP_SIZE = s
            cs.cuckoo_search(opt_func, verbose=False)
            data = pd.read_csv('results/results_cs.csv', header=None)
            final_mean = data[len(data.columns) - 1].mean()
            print(f'|{l:4} |{s:5} | {round(final_mean, 4)} |')


def pso_tune(opt_func):
    omega = [0.5, 0.6, 0.7]
    phi_g = [0.25, 0.5, 0.75, 1]
    phi_p = [0.1, 0.25, 0.5, 0.75, 1]

    print('|  ω  |  φ₁  |  φ₂   | Resultado |')
    print('|-----|------|------|-----------|')
    for o in omega:
        pso.OMEGA = o
        for pg in phi_g:
            pso.PHI_G = pg
            for pp in phi_p:
                pso.PHI_P = pp
                pso.particle_swarm_opt(opt_func, verbose=False)
                data = pd.read_csv('results/results_pso.csv', header=None)
                final_mean = data[len(data.columns) - 1].mean()
                print(f'|{o:4} |{pg:5} | {pp:5} |{round(final_mean, 4)} |')


def wilcoxon(opt_func, population_size, dimensions):
    cs.POPULATION_SIZE = population_size
    pso.POPULATION_SIZE = population_size
    cs.DIMENSIONS = dimensions
    pso.DIMENSIONS = dimensions

    cs.cuckoo_search(opt_func, verbose=False)
    pso.particle_swarm_opt(opt_func, verbose=False)

    data_cs = pd.read_csv('results/results_cs.csv', header=None)
    last_iter_cs = data_cs[len(data_cs.columns) - 1].to_list()

    data_pso = pd.read_csv('results/results_pso.csv', header=None)
    last_iter_pso = data_pso[len(data_pso.columns) - 1].to_list()

    print(
        f'{opt_func.func.__name__} Dimensions: {dimensions}',
        f'Population: {population_size}',
        ranksums(last_iter_cs, last_iter_pso)
    )


if __name__ == "__main__":
    # cs_tune(bm.schwefel)
    # print('\n\n')
    # cs_tune(bm.function_3)

    # pso_tune(bm.schwefel)
    # print('\n\n')
    # pso_tune(bm.function_3)

    # cs.cuckoo_search(bm.schwefel)
    # pso.particle_swarm_opt(bm.schwefel)

    wilcoxon(bm.schwefel, 100, 2)
    wilcoxon(bm.function_3, 100, 2)
    wilcoxon(bm.schwefel, 100, 10)
    wilcoxon(bm.function_3, 100, 10)