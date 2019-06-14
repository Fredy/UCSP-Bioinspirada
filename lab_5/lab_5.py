import benchmarks as bm
import cuckoo_search as cs
import particle_swarm_opt as pso
import operator

if __name__ == "__main__":
    cs.cuckoo_search(bm.function_3)
    # pso.particle_swarm_opt(bm.function_3)
