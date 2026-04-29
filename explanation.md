La cuadratura Gaussiana es un método de integración numérico basado en
puntos de muestreo no uniformes obtenidos a partir de los ceros de los
polinomios de Legendre. Utilizando $N$ puntos, el método es exacto para
polinomios de hasta grado $2N-1$, lo que se puede demostrar ser el mayor
grado posible.

El error de la cuadratura gaussiana decrece como $c/N^2$, por lo que su
convergencia suele ser rápida, aunque se debe tomar en cuenta el costo
computacional de calcular los ceros del polinomio. Además, al usar un
menor número de puntos, funciones "mal portadas" suelen ser problemáticas.
