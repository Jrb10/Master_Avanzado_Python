# sintaxis funcion lambda
# lambda parametros: expresion
cuadrado=lambda x: x**2
print(cuadrado(2))

def cuadrado1(x):
    return x**2
print(cuadrado1(2))

# map
# map(una funcion,una lista)
enteros=[1,2,3,4]
cuadrados=list(map(lambda x: x**2, enteros))
print(cuadrados)

def funcion_cuadrado(x):
    return x**2
def funcion_cubo(x):
    return x**3
funciones=[funcion_cuadrado,funcion_cubo]  
for e in enteros:
    valores=list(map(lambda x: x(e),funciones))
    print(valores)

# filter
# filter(una funcion,una lista) solo los valores true
enteros1=[1,2,3,4]
pares=list(filter(lambda x: x%2==0, enteros1))
print(pares)

# reduce ( calculo acumulativo )
from functools import reduce
# reduce(una funcion,una lista) solo los valores true
# el que coge la suma  y   el otro el que se va pasando x=15 e y= 1,2,3,4
suma=reduce( lambda x, y: x+y, valores)
print(suma)

