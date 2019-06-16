# Algoritmos de enjambre de partículas

En este laboratorio se compararon dos algoritmos de ejambre de párticulas:

- Cuckoo Search via Lévy Flights (CS) `[Yang and Deb, 2009]`
- Particle Swarm Optimization (PSO) `[Kennedy and Eberhart, 1995]`

## Cuckoo Search via Lévy Flights (CS)

Este algoritmo se basa en el comportamiento parasitario de algunas especies de aves cuco (_Cuckoo_), combinado con Lévy Flights. Las aves cuco tienden a depositar sus huevos en los nidos de otras aves. Los huevos de los cucos eclosionan antes de los del ave anfitriona. Por instinto, al eclosionar, la cría trata de arrojar los huevos del ave anfitrión fuera del nido. De esta forma la cría de cuco puede obtener todo el alimento suministrado por el ave anfitriona.

Por otro lado, Lévy flight, es un tipo de paseo aleatoria, en los cuales el tamaño de los pasos sigue una distribución de probabilidad _heavy-tailed_ (se acerca más rápido a cero que la distribución exponencial). Este comportamiento es realizado por muchos animales e insectos en la naturaleza.

### Funcionamiento

Este algoritmo sigue tres reglas:

1. Cada cuco deposita un huevo en un nido elegido de forma aleatoria.
2. Los mejores nidos, que tienen huevos de buena calidad, se mantienen en siguientes generaciones.
3. La cantidad de nidos disponible es fija, y la probabilidad de que el ave anfitriona descubra el huevo de cuco es _Pa_ ∈ [0, 1]. En este caso, el nido es abandonado.

Cada nido representa una solución, y un huevo de cuco representa un elemento de una solución. El objetivo es usar las nuevas soluciones (potencialmente buenas) para reemplazar las soluciones que no son tan buenas en los nidos.

Cada vez que se genera una nueva solución _X_, se realiza un _Leví Fligh_:

![equación](<https://latex.codecogs.com/svg.latex?x_i^{(t+1)}%20%3D%20x_i^{(t)}%20+%20\alpha%20\oplus%20\text{Levy}(\lambda)>)

Donde _a_ > 0 y representa el tamaño del paso a tomar y está relacionado a la escala del problema de interés. Un paseo aleatorio es una cadena de Markov, donde el siguiente estado depende únicamente de la ubicación actual (primer término de la ecuación anterior) y la probabilidad de transición (segundo término)

### Modelamiento

- Se usaron las funciones de benchmark como las funciones objetivo de este algoritmo.
- Cada nido representa una solución, los huevos de cada nido representan cada elemento _x_ de la solución.

## Particle swarm optimization

Es un algoritmo usado para optimizar un problema, mejorando la solución candidata iteratibamente. Este algoritmo está inspirado en el comportamiento social de bandadas de aves y cardúmenes. Cada uno de los individuos puede beneficiarse por los descubrimientos y experiencia de los otros miembros de la población.

### Funcionamiento

Se tiene una población de soluciones candidatas, llamadas partículas, que se mueven dentro de un espacio de búsqueda. Para esto se aplica una fórmula sobre la posición y velocidad de estas partículas.
Cada uno de los individuos se ve atraído a un punto en concreto (lugar de descanzo) y siguen un comportamiento similar a los _Boids_:

- Todos son atraidos por un punto en concreto.
- Recuerdan cuando han estado cerca de este punto.
- Comparten información con sus vecinos sobre la ubicación del punto en concreto.

El movimiento de cada partícula se ve influenciado por la mejor posición conocida por la partícula y la mejor solución global. Cada partícula se ubica en una posición del espacio de búsqueda y su _fitness_ representa la calidad de su posición. Las partículas se mueven a una velocidad determinada. Además de tener un estado interno, comparten un estado global con el resto de partículas.

En cada iteración se usa la siguiente fórmula para modificar la velocidad _v_ de cada partícula:

![equación](<https://latex.codecogs.com/svg.latex?v_i^{t+1}%3Dv_i^t%20+\phi_1U_1^t(\text{pb}_i^t-p_i^t)+\phi_2U_2^t(\text{gb}_i^t-p_i^t)>)

Donde el primer termino representa a la incercia (velocidad actual), el segúndo termino es la influencia personal y el tercer término es la influencia global. El primero permite que la partícula se mueva en la misma dirección con la misma velocidad; el segundo, hace que la partícula tienda a regresar a una posición previa, mejor que la actual; y el tercero, permite a la partícula seguir la mejor dirección encontrada en la población. Por otro lado, el primer término permite la explotación y el seguno y tercer termino permiten la exploración. Ambos _ϕ_ son constantes, _U_ son números aleatorios en el rango _[0,1[_, _pb_ representa la mejor posición personal y _gb_ la mejor posición global, _p_ y _v_ son la posición y velocidad respectivamente.

### Modelamiento

- Se usaron las funciones de benchmark como las funciones objetivo de este algoritmo.
- Cada una de las posiciones de las partículas representa una solución. Tanto la posición como la velocidad son inicializadas con valores aleatorios.

## Ajuste de párametros

Para realizar el ajuste de parámetros se realizaron 20 ejecuciones de 50 iteraciones cada, para promediar el resultado obtenido al finalizar la ejecución.

### Cuckoo Search

En Cuckoo Search los parámetros son los siguientes:

- Constante Lambda (λ): influye en la generación aleatoria de tamaños de pasos para _Lévy flight_ `1 < λ ≤ 3`
- Tamaño de paso (α): dependiente del problema a optimizar `α > 1`
- Tamaño de la población(_n_): cantidad de individuos que conforman la población.
- Probabilidad de abandono (_Pa_): probabilidad de que se abandone una solución (huevo) `Pa ∈ [0,1]`

En el trabajo en el que se presenta este algoritmo se usan _n_ = 15 y _Pa_ = 0.25, y se menciona que estos parámetros no afectan mucho a la convergencia, por lo que un ajuste fino de estos no es necesario para la mayoría de problemas. También se menciona que α = 1 se puede usar en la mayoría de casos.

Se usa el mismo valor para _Pa_ mencionado anteriormente y _n_ = 50 y se buscan los mejores valores para λ y α.

Para α se prueban:

- 0.01
- 0.5
- 1

Para λ se prueban:

- 1.1
- 1.5
- 2
- 2.5
- 3

Se elegirá la combinación que alcance una mejor respuesta luego de 50 iteraciones.

#### Schwefel: minimización (2 dimensiones)

En la siguiente tabla se muestran las pruebas realizadas con distintos valores para λ y α.

| λ   | α    | Resultado  |
| --- | ---- | ---------- |
| 1.1 | 0.01 | 2.2285     |
| 1.1 | 0.5  | **0.1491** |
| 1.1 | 1    | 0.1587     |
| 1.5 | 0.01 | 4.1164     |
| 1.5 | 0.5  | **0.1227** |
| 1.5 | 1    | 0.1425     |
| 2   | 0.01 | 4.9007     |
| 2   | 0.5  | 0.0657     |
| 2   | 1    | **0.0592** |
| 2.5 | 0.01 | 3.4754     |
| 2.5 | 0.5  | **0.0937** |
| 2.5 | 1    | 0.2661     |
| 3   | 0.01 | 3.5762     |
| 3   | 0.5  | **0.4188** |
| 3   | 1    | 0.1525     |

Se puede ver que la mayoría de casos α = 0.5 da los mejores resultados, en la siguiente tabla están los resultados usando α = 0.5 y se puede observar que con λ = 2 se produce la mejor respuesta:

| λ   | α   | Resultado  |
| --- | --- | ---------- |
| 1.1 | 0.5 | 0.1491     |
| 1.5 | 0.5 | 0.1227     |
| 2   | 0.5 | **0.0657** |
| 2.5 | 0.5 | 0.0937     |
| 3   | 0.5 | 0.4188     |

# Función 3: maximización (2 dimensiones)

En la siguiente tabla se muestran las pruebas realizadas con distintos valores para λ y α.

| λ   | α    | Resultado  |
| --- | ---- | ---------- |
| 1.1 | 0.01 | 0.9688     |
| 1.1 | 0.5  | 0.9731     |
| 1.1 | 1    | **0.9755** |
| 1.5 | 0.01 | 0.9763     |
| 1.5 | 0.5  | 0.9775     |
| 1.5 | 1    | **0.9776** |
| 2   | 0.01 | 0.9636     |
| 2   | 0.5  | **0.9744** |
| 2   | 1    | 0.972      |
| 2.5 | 0.01 | **0.9765** |
| 2.5 | 0.5  | 0.9685     |
| 2.5 | 1    | 0.9725     |
| 3   | 0.01 | 0.9667     |
| 3   | 0.5  | 0.9722     |
| 3   | 1    | **0.9732** |

En la mayoría de casos, se obtiene la mejor respuesta usando α = 1, aunque con α = 0.5 se obtienen respuestas muy similares. Por conveniencia también se usará α = 0.5. En la siguiente tabla se muestran los resultados usando α = 0.5. Con distintos λ, el resultado es muy similar, debido a esto y por conveniencia se usará λ = 2.

| λ   | α   | Resultado |
| --- | --- | --------- |
| 1.1 | 0.5 | 0.9731    |
| 1.5 | 0.5 | 0.9775    |
| 2   | 0.5 | 0.9744    |
| 2.5 | 0.5 | 0.9685    |
| 3   | 0.5 | 0.9722    |

### Particle swarm optimization (PSO)

En PSO los parámetros son los siguientes

- Tamaño de la población(_n_): cantidad de individuos que conforman la población.
- Inercia (ω): afecta el movimiento de la partícula dada su último valor de velocidad. `ω ∈ [0.5, 0.9]`
- Coeficientes de aceleración global y local(φ₁, φ₂): representan la importancia que se le dará a la mejor posición personal y a la mejor posición global. `φ₁, φ₂ ∈ [0, 1]`

Al igual que el algoritmo anterior, el tamaño de población es de 50 individuos.

Para ω se prueban:

- 0.5
- 0.6
- 0.7
- 0.8
- 0.9

Para φ₁, φ₂ se prueban:

- 0.1
- 0.25
- 0.5
- 0.75
- 1

Se elegirá la combinación que alcance una mejor respuesta luego de 200 iteraciones.

#### Schwefel: minimización (2 dimensiones)

La tabla completa se puede observar en [este archivo](tables/pso_tune.md).

En la siguiente tabla se muestran los resultados de las pruebas realizadas con distintos valores para ω, φ₁, φ₂ . En esta tabla solo se consideraron los resultados que más se acercan al mínimo global de la función evaluada.

| ω   | φ₁   | φ₂   | Resultado |
| --- | ---- | ---- | --------- |
| 0.5 | 0.25 | 0.5  | 0.7107    |
| 0.5 | 0.25 | 0.75 | 0.5314    |
| 0.5 | 0.5  | 0.1  | 0.0109    |
| 0.5 | 0.5  | 0.25 | 0.017     |
| 0.5 | 0.5  | 0.75 | 0.131     |
| 0.5 | 0.5  | 1    | 0.1243    |
| 0.5 | 0.75 | 0.1  | 0.0026    |
| 0.5 | 0.75 | 0.25 | 0.0354    |
| 0.5 | 0.75 | 0.75 | 0.1604    |
| 0.5 | 0.75 | 1    | 0.1884    |
| 0.5 | 1    | 0.25 | 0.0313    |
| 0.5 | 1    | 0.5  | 0.2805    |
| 0.5 | 1    | 0.75 | 0.7545    |
| 0.6 | 0.25 | 0.25 | 0.323     |
| 0.6 | 0.25 | 0.5  | 0.9194    |
| 0.6 | 0.25 | 1    | 0.9029    |
| 0.6 | 0.5  | 0.5  | 0.1334    |
| 0.6 | 0.75 | 0.1  | 0.2361    |
| 0.6 | 0.75 | 0.5  | 0.4567    |
| 0.6 | 0.75 | 0.75 | 0.8897    |
| 0.6 | 1    | 0.1  | 0.1567    |
| 0.6 | 1    | 0.25 | 0.2308    |
| 0.7 | 0.25 | 0.1  | 0.3434    |
| 0.7 | 1    | 0.25 | 0.8546    |

Los mejores resultados se obtuvieron con ω = 0.5, en especial las combinaciones en las que φ₁ > φ₂, lo que indica que influcenciarse de la mejor posición global es benificioso para los individuos
Realizando más experimentos se encontró que la mejor combinación es ω = 0.5, φ₁ = 0.75 y φ₂ = 0.25.

# Función 3: maximización (2 dimensiones)

La tabla completa se puede observar en [este archivo](tables/pso_tune_2.md).

En la siguiente tabla se muestran los resultados de las pruebas realizadas con distintos valores para ω, φ₁, φ₂ . En esta tabla solo se incluyeron los resultados que más se acercan al máximo global de la función evaluada

| ω   | φ₁   | φ₂   | Resultado |
| --- | ---- | ---- | --------- |
| 0.5 | 0.5  | 0.1  | 0.9915    |
| 0.5 | 0.5  | 0.25 | 0.9909    |
| 0.5 | 0.5  | 0.5  | 0.9905    |
| 0.5 | 0.75 | 0.1  | 0.992     |
| 0.5 | 0.75 | 0.25 | 0.9912    |
| 0.5 | 0.75 | 0.5  | 0.9905    |
| 0.5 | 0.75 | 0.75 | 0.9903    |
| 0.5 | 1    | 0.1  | 0.9912    |
| 0.5 | 1    | 0.25 | 0.9911    |
| 0.6 | 0.25 | 0.1  | 0.9907    |
| 0.6 | 0.5  | 0.1  | 0.9904    |
| 0.6 | 0.5  | 0.25 | 0.9906    |
| 0.6 | 0.75 | 0.1  | 0.9904    |
| 0.6 | 0.75 | 0.25 | 0.991     |

Los resultados de la tabla son muy similares entre sí, por esto se eligieron los mismos valores empleados en la anterior evaluación: ω = 0.5, φ₁ = 0.75 y φ₂ = 0.25.

## Comparación usando prueba de suma de rangos de Wilcoxon

| Función   | Dimensiones | Statics  | P value     |
| --------- | ----------- | -------- | ----------- |
| Schwefel  | 2           | 4.11161  | 3.92903e-05 |
| Schwefel  | 10          | -4.73376 | 2.20392e-06 |
| Función 3 | 2           | -5.41001 | 6.30184e-08 |
| Función 3 | 10          | 5.05836  | 4.22862e-07 |
