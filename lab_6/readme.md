# Reinforcement Learning: Q-Learning

En este trabajo se implementó y se verifico el funcionamiento de la estrategia _Q-learning_ a través de pruebas que son explicadas a continuación.

## Selección de α y γ

Para comprobar qué combinación de α y γ ofrece una mejor convergencia se probaron valores de α, γ en el rango _[0, 1]_ con un incremento de _0.1_ (_0, 0.1 , ... , 1_). El tamaño del grid es de 100x100, el punto de inicio es el punto central y el punto objetivo es la esquina inferior izquiera. Si luego de 1000 iteraciones no se llega al objetivo, la posición del agente se reinicia en el punto inicial, manteniendo los pesos de _Q(s,a)_. Se ejecutó el algortimo 20 veces y se promedió el total de iteraciones requeridas para llegar al punto objetivo. La tabla completa se encuentra en [este archivo](table.md). La siguiente tabla solo considera los mejores resultados de cada α:

| α   | γ   | Iteraciones promedio |
| --- | --- | -------------------- |
| 0.0 | 0.0 | 1295678.4            |
| 0.1 | 0.4 | 162339.2             |
| 0.2 | 0.6 | 199081.8             |
| 0.3 | 0.8 | 82870.6              |
| 0.4 | 0.6 | 167877.8             |
| 0.5 | 0.4 | 132173.4             |
| 0.6 | 0.6 | 126133.0             |
| 0.7 | 0.3 | 107149.6             |
| 0.8 | 0.8 | 124183.4             |
| 0.9 | 0.8 | 92906.6              |
| 1.0 | 0.1 | 85318.0              |

Observando la tabla completa, se aprecia que cuando α > 5 las iteraciones empiezan a decrecer, requiriendo al rededor de 100000 iteraciones para alcanzar el objetivo. Para todas las pruebas siguientes se escogeron los valores **α = 1.0** y **γ = 0.1**

## Diferencias en tamaño de grid

Se usaron los parámetros seleccionados en las pruebas anteriores y se probaron distintos tamaños de grid. Al igual que la anterior prueba, se ejecutó el algoritmo 20 veces, por cada tamaño, y se promedió el total de iteraciones.

| Tamaño del grid | Iteraciones promedio |
| --------------- | -------------------- |
| 10x10           | 193.8                |
| 20x20           | 294.2                |
| 30x30           | 2227.2               |
| 40x40           | 5077.6               |
| 50x50           | 9785.8               |
| 60x60           | 12913.8              |
| 70x70           | 35373.2              |
| 80x80           | 41201.8              |
| 90x90           | 84542.4              |
| 100x100         | 122191.6             |

En la tabla se hace evidente que mientras mayor es el tamaño del grid, más iteraciones son necesarias para llegar al punto objetivo.
