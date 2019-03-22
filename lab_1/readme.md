# Lab 1


## Setup

Para ejecutar el código:

**Es necesario python 3.6+**

1. Clonar el repo.
2. entrar a la carpeta `lab_1`
3. Ejecutar `python lab_1.py`

### 1. Código

### 2. Entropía de un segmento de texto

```
----text_1.txt----
Hartley: 5.0444
Shannon: 4.0948
----text_2.txt----
Hartley: 5.0444
Shannon: 4.1034
----text_3.txt----
Hartley: 5.0444
Shannon: 4.123
```

* Los textos tienen la misma entropía de Hartley, porque
el total de elementos alfabeto usado es el mismo: letras en español + letras
con acentos + espacio (27 + 5 + 1)
* La entropía de Shannon es similar en todos porque todos los textos
están escritos en español.

### 3. Lipogramas

Un lipograma es un juego de palabras que consiste en escribir un texto sin
usar una letra en particular o un conjunto de letras.[[Wiki]](https://en.wikipedia.org/wiki/Lipogram)

```
----lipogram_1.txt----
Hartley: 5.0444
Shannon: 4.0311
----lipogram_2.txt----
Hartley: 5.0444
Shannon: 3.9846
```

Se nota mayor diferencia en el valor de la entropía de Shannon, debido a que
en estos textos no se ha usado una o más letras, en el primero no se
usaron `e, k, é`, en el segundo no se usaron `k, w, z, á`

Ya que para calcular la entropía de Hartley se están considerando las letras
que tienen cero ocurriencias y se usa el mismo alfabeto para todos los
textos, este valor es el mismo.

### 4. Generación de textos

```
----random_no_weights.txt----
Hartley: 5.0444
Shannon: 5.0358
----random_weights.txt----
Hartley: 5.0444
Shannon: 4.1118
```

La gran diferencia entre los valores de entropias de Shannon de los textos
generados se debe a que en el generado aleatoriamente todos los caracteres
del alfabeto tienen la misma posibilidad de aparecer en el texto, en cambio
en el segundo, que usa los pesos de uno de los textos "normales", la
distribución de letras es más real o "normal".

Al observar los textos, el generado aleatoriamente carece de sentido alguno y
el segundo parace un poco más real.

### 5. Permutación

```
----text_1.txt----
Hartley: 5.0444
Shannon: 4.0948
----shuffled_text_1.txt----
Hartley: 5.0444
Shannon: 4.0948
```

Otra vez, el valor de la entropía de Hartley es el mismo porque en todos el
alfabeto es el mismo. El valor de Shannon es el mismo porque cada caracter
tiene la misma recurrencia en los dos textos.