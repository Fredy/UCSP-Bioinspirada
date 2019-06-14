# Algoritmos de enjambre de partículas

En este laboratorio se compararon dos algoritmos de ejambre de párticulas:
* Cuckoo Search via Lévy Flights (CS) `[Yang and Deb, 2009]`
* Particle Swarm Optimization (PSO) `[Kennedy and Eberhart, 1995]`

## Cuckoo Search via Lévy Flights (CS)

Este algoritmo se basa en el comportamiento parasitario de algunas especies de aves cuco (_Cuckoo_), combinado con Lévy Flights. Las aves cuco tienden a depositar sus huevos en los nidos de otras aves. Los huevos de los cucos eclosionan antes de los del ave anfitriona. Por instinto, al eclosionar, la cría trata de arrojar los huevos del ave anfitrión fuera del nido. De esta forma la cría de cuco puede obtener todo el alimento suministrado por el ave anfitriona.

Por otro lado, Lévy flight, es un tipo de paseo aleatoria, en los cuales el tamaño de los pasos sigue una distribución de probabilidad _heavy-tailed_ (se acerca más rápido a cero que la distribución exponencial). Este comportamiento es realizado por muchos animales e insectos en la naturaleza.

### Funcionamiento

Este algoritmo sigue tres reglas:
1. Cada cuco deposita un huevo en un nido elegido de forma aleatoria.
2. Los mejores nidos, que tienen huevos de buena calidad, se mantienen en siguientes generaciones.
3. La cantidad de nidos disponible es fija, y la probabilidad de que el ave anfitriona descubra el huevo de cuco es _Pa_ ∈ [0, 1]. En este caso, el nido es abandonado.

Cada huevo en un nido representa una solución, y un huevo de cuco representa una nueva solución. El objetivo es usar las nuevas soluciones (potencialmente buenas) para reemplazar las soluciones que no son tan buenas en los nidos.

Cada vez que se genera una nueva solución _X_, se realiza un _Leví Fligh_:

![equación](https://latex.codecogs.com/svg.latex?x_i^{(t&plus;1)}%20%3D%20x_i^{(t)}%20&plus;%20\alpha%20\oplus%20\text{Levy}(\lambda))

Donde _a_ > 0 y representa el tamaño del paso a tomar y está relacionado a la escala del problema de interés. Un paseo aleatorio es una cadena de Markov, donde el siguiente estado depende únicamente de la ubicación actual (primer término de la ecuación anterior) y la probabilidad de transición (segundo término)

### Modelamiento

* Se usaron las funciones de benchmark como las funciones objetivo de este algoritmo.
* Cada nido representa una solución, los huevos de cada nido representan cada elemento _x_ de la solución.

## Particle swarm optimization

Es un algoritmo usado para optimizar un problema, mejorando la solución candidata iteratibamente. Este algoritmo está inspirado en el comportamiento social de bandadas de aves y  cardúmenes. Cada uno de los individuos puede beneficiarse  por los descubrimientos y experiencia de los otros miembros de la población.

### Funcionamiento

Se tiene una población de soluciones candidatas, llamadas partículas, que se mueven dentro de un espacio de búsqueda. Para esto se aplica una fórmula sobre la posición y velocidad de estas partículas. 
Cada uno de los individuos se ve atraído  a un punto en concreto (lugar de descanzo) y siguen un comportamiento similar a los _Boids_:
* Todos son atraidos por un punto en concreto.
* Recuerdan cuando han estado cerca de este punto.
* Comparten información con sus vecinos sobre la ubicación del punto en concreto.

El movimiento de cada partícula se ve influenciado por la mejor posición conocida por la partícula y la mejor solución global. Cada partícula se ubica en una posición del espacio de búsqueda y su _fitness_ representa la calidad de su posición. Las partículas se mueven a una velocidad determinada. Además de tener un estado interno, comparten un estado global con el resto de partículas.

En cada iteración se usa la siguiente fórmula para modificar la velocidad _v_ de cada partícula:

![equación](https://latex.codecogs.com/svg.latex?v_i^{t&plus;1}%3Dv_i^t%20&plus;\phi_1U_1^t(\text{pb}_i^t-p_i^t)&plus;\phi_2U_2^t(\text{gb}_i^t-p_i^t))

Donde el primer termino representa a la incercia (velocidad actual), el segúndo termino es la influencia personal y el tercer término es la influencia global. El primero permite que la partícula se mueva en la misma dirección con la misma velocidad; el segundo, hace que la partícula tienda a regresar a una posición previa, mejor que la actual; y el tercero, permite a la partícula seguir la mejor dirección encontrada en la población. Por otro lado, el primer término permite la explotación y el seguno y tercer termino permiten la exploración. Ambos _ϕ_ son constantes, _U_ son números aleatorios en el rango _[0,1[_, _pb_ representa la mejor posición personal y _gb_ la mejor posición global, _p_ y _v_ son la posición y velocidad respectivamente.  