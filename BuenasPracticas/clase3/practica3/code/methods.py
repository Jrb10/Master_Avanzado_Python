""" 
    Este script contiene diferentes funciones

    *Funciones*
    ---------------
    addName:
        Funcion para añadir un nombre

    addNumber:
        Funcion para comprobar el numero de digitos del telefono

    checkMoney:
        Metodo para mostrar el saldo de una persona

    *Ejemplo*
    ^^^^^^^^^^^^^
    >>>addName('Jonathan')


"""

class InvalidName(Exception):
    """Clase que trata el error de nombre repetido

    Args:
        Exception (InvalidName): Error si ya existe el nombre
    """
    pass
class InvalidQuery(Exception):
    """Clase que trata el error de busqueda no valida

    Args:
        Exception (InvalidQuery): Consulta no valida, no existe la persona
    """
    pass

def addName(name:str):
    """Funcion que añade un nombre a la lista

    :param name: Nombre que se pasa como argumento
    :type name: :class:`str`
    :raises TypeError: Error si no se pasa una cadena
    :raises InvalidName: Error si ya existe el nombre
    :return: Devuelve la cadena con el nombre añadido
    :rtype: :class:`list`

    """
    names=['Juan','Pepe','Lucia']
    if isinstance(name,str) & (name not in names):
        names.append(name)
        return names
    elif not isinstance(name,str):
        raise TypeError("Incorrect type data")
    elif name in names:
        raise InvalidName("The name exists")


def addNumber(number:int):
    """Funcion que comprueba que el telefono que insertas tiene 9 digitos

    :param number: Numero que se pasa como argumento
    :type number: :class:`int`
    :return: Devuelve True si es correcto
    :rtype: :class:`bool`

    """
    phone=str(number)
    if len(phone)==9:
        return True

  
def checkMoney(name:str):
    """Funcion que te muestra el saldo que tiene la persona

    :param name: Nombre de la persona que se pasa como argumento
    :type name: :class:`str`
    :raises InvalidQuery: Consulta no valida, no existe la persona
    :return: Devuelve el saldo de la persona
    :rtype: :class:`int`

    """
    bill={'Ruben':100,'Jonathan':150}
    for c,v in bill.items():
        if c==(name):
            return v 
        else:
            raise InvalidQuery("Error, the query could not be done")



