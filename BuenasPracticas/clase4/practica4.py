import pdb
pdb.set_trace()

'''
    Practica 4: 
    1- EEl programa debe devolver el mayor elemento de cada sublista 
    (señalado en negrita)
    2- Usando la funcion filter-- obtener los numeros primos de una lista
'''

class bold_color:
    """Para escribir en negrita, tiene que tener un inicio y un fin 
    """
    BOLD = '\033[1m'
    END = '\033[0m'

def max_value(e:list):
    """Funcion que devuelve el valor maximo de cada sublista

    Args:
        e (list): sublista de la lista principal

    Returns:
        int: numero maximo de cada sublista
    """
    return max(e)

def max_element(ele:list):
    """Funcion que muestra el mayor elemento de cada sublista

    Args:
        ele (list): lista que se pasa por parametro
    """
    cadena=list(i for i in ele)
    print("Lista inicial: ", cadena)

    # usando join para convertir list a str y la clase bold_color
    # break 44 --
    # continue-- para que llegue al punto de parada
    # list -- para ver el codigo antees y despues de la parada
    # next -- para que vaya paso a paso
    # p max(sublista) -- para consultar el valor de la variable
    # next ---
    # p max(sublista) -- para consultar el valor de la variable
    # next --- Nos muestra el resultado 
    max_values =','.join([str(max(sublista)) for sublista in ele])
    print("1-opcion: El resultado en negrita es : " + bold_color.BOLD + max_values +bold_color.END)

def max_element1(ele1:list):
    """Funcion que muestra el mayor elemento de cada sublista usando map

    Args:
        ele1 (list): lista que se pasa por parametro
    """
    # utilizando map y la funcion max_value
    max_values2=list(map(max_value,ele1))
    max_values2=str(max_values2)
    print("2-opcion: El resultado en negrita es : ",'\033[1m' + max_values2 + '\033[0m')    

def num_primos(lista: list):
    """Funcion que muestra los numeros primos de una lista

    Args:
        lista (list): lista que se pasa por parametro
    """
    num=list(x for x in lista)
    prime_number=list(filter(lambda x: x%2!=0, lista))
    print(f'De la lista {num} son numeros primos : {prime_number}')

if __name__=='__main__':
    max_element([[1,5,3],[10,2]])
    max_element1([[1,5,5,3],[10,2]])
    num_primos([3,4,8,5,5,22,13])
