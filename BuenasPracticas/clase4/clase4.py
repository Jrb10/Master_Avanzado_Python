
cuadrados=[i**2 for i in range(5)]
print(cuadrados)

cuadrados1=[]
for i in range(5):
    cuadrados1.append(i**2)
print(cuadrados1)

# sintaxis
# lista= [ expresion for elemento in iterable]

def al_cuadrado(i):
    return i**2
cuadrados2=[al_cuadrado(i) for i in range(5)]

lista=[1,2,3,4]
new_list=[i**2 for i in lista]
print(new_list)

# condiciones
# lista=[expresion for elemento in interable if condicion]

frase="hola mundo"
letra_o= [i for i in frase if i=='o']
print(letra_o)

# conjuntos
letra_o={i for i in frase if i=='o'}

#compresion de diccionarios
lista1=[1,2,3]
lista2=['a','b','c']
my_dic={ i:j for i,j in zip(lista1,lista2)}
print(my_dic)

