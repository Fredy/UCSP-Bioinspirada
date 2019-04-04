# Lab 1


## Setup

Para ejecutar el código:

**Es necesario python 3.6+**

1. Clonar el repo.
2. Instalar dependencias (`Pipfile`)
2. Entrar a la carpeta `lab_2`
3. Ejecutar `python lab_2.py`
4. Para generar el gráfico ejecutar: `python charts.py`

## Comparación entre estragias evolutivas

En este laboratorio se implementaros tres estrategias evolutivas:

* (1 + 1)-EE
* (μ + λ)−EE
* (μ, λ)−EE

Para la comparación se realizaron 40 iteraciones de cada algoritmo. Esto se realizó 20 veces para obtener un promedio de los mejores fitness de cada algoritmo.

En el siguiente gráfico se pueden observar las curvas de mejores elementos de cada uno de los algoritmos implementados.

![Curva de mejores elementos]()

Se puede observar que tanto `(1 + 1)-EE` y `(μ + λ)−EE` van mejorando en cada generación. En el primero ocurre debido a que siempre se mantiene el elemento con el mejor fitness. En el seguno, esto ocurre porque siempre se mantienen los mejores elementos entre los padres e hijos. 

En cambio, `(μ, λ)−EE` no converge, debido a que en cada generación solo se mantienen los mejores elementos de los hijos y los padres son descartados.