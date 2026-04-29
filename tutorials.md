Suponga que se desea evaluar la integral:
$$
\int_1^2 \frac{x^3}{e^x -1} dx
$$
Para ello, se implementa la función en Python (utilizando `NumPy`):
``` python
import numpy as np

def funcInt(x):
    return x**3/(np.exp(x)-1)
```
Ahora, se calculan los puntos y los pesos con el valor de $N$ a utilizar.
en este caso 10:
``` python
import cuadrature

x, w = cuadrature.gausssxw(10)
```
Se escalan los pesos y los puntos al intervalo deseado ($[0,2]$):
``` python
xe, we = cuadrature.gaussab(0, 2, x, w)
```
Finalmente se evalua la integral:
``` python
np.sum(funtInt(xe)*we)
>>> 1.176
```
