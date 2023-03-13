""" Primer problema de la prueba tecnica para Data Observatory """

# 1 Dada una patente retornar el id asociado (llave primaria)
# 2 Dado un ID (llave primaria) Retornar la patente asociada.

# Imports
import string  # para obtener digitos y letras

# diccionario con la asociacion de letra a numero
# Hacemos una lista con todas las letras
x = [letter for letter in string.ascii_uppercase]
# Pasamos esa lista a un diccionario que las asocia a un numero
letras_a_num: dict = dict(zip(x, map(x.index, x)))
# La lista inversa nos ayudara con la siguiente parte
num_a_letras = {v: k for k, v in letras_a_num.items()}
# Todas estas asociaciones se ocupan independientemente de cuantas veces llamemos
# a las funciones, por lo que vale la pena mantenerlas en memoria precomputadas
# en vez de computarlas cada vez que llamemos a una funcion


def patente_a_id(patente: str) -> int:
    """ Pasa de una patente (en string) a un ID (en int)
        Se asume una patente de la forma [A-Z]{4}[0-9]{3} """
    letras = patente[0:4]
    numeros = int(patente[4::])
    id_patente = 0

    for i, letra in enumerate(reversed(letras)):
        id_patente += letras_a_num[letra]*(10**(i+3))
    id_patente += numeros + 1

    return id_patente


def id_a_patente(id_patente: int) -> str:
    """ Pasa de un ID (en int) a una patente (en string). 
        Se asume una patente de la forma [A-Z]{4}[0-9]{3} """
    numero = int(str(id_patente)[-3::]) - \
        1 if int(str(id_patente)[-3::]) - 1 != -1 else 999
    potencias = id_patente - numero
    potencias //= 1000
    indices = str(potencias)
    resultado = ""
    for i in indices:
        resultado += num_a_letras[int(i)]
    # Rellenamos con A's si es que el num era chico
    resultado = resultado.rjust(4, "A")
    # appendeamos el numero de la patente (rellenando con 0s)
    resultado += str(numero).rjust(3, "0")
    return resultado


# Pruebas simples
assert patente_a_id("AAAA000") == 1
assert patente_a_id("AAAB000") == 1001
assert patente_a_id("AABA023") == 10024
assert patente_a_id("AAAA999") == 1000

assert id_a_patente(1) == "AAAA000"
assert id_a_patente(1001) == "AAAB000"
assert id_a_patente(10024) == "AABA023"
assert id_a_patente(1000) == "AAAA999"
