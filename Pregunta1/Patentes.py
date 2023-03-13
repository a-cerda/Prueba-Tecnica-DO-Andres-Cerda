# Primer problema de la prueba tecnica para Data Observatory

# 1 Dada una patente retornar el id asociado (llave primaria)
# 2 Dado un ID (llave primaria) Retornar la patente asociada.

# Imports
import string # para obtener digitos y letras
import re # para formular la expresion regular

#posibles_patentes = 
# diccionario con la asociacion de letra a numero
x = [letter for letter in string.ascii_uppercase] # Hacemos una lista con todas las letras
letras_a_num: dict = dict(zip(x, map(x.index, x))) # Pasamos esa lista a un diccionario que las asocia a un numero
num_a_letras = {v: k for k, v in letras_a_num.items()} # La lista inversa nos ayudara con la siguiente parte
# Todas estas asociaciones se ocupan independientemente de cuantas veces llamemos a las funciones, por lo que vale
# la pena mantenerlas en memoria precomputadas en vez de computarlas cada vez que llamemos a una funcion

# Pasa de una patente (en string) a un ID (en int)
# Se asume una patente de la forma [A-Z]{4}[0-9]{3}
def Patente_A_ID(patente: str) -> int:
    letras = patente[0:4]
    numeros = int(patente[4::])
    ID = 0

    for i, letra in enumerate(reversed(letras)):
        ID += letras_a_num[letra]*(10**(i+3))
    ID += numeros + 1

    return ID

# Pasa de un ID (en int) a una patente (en string)
# Se asume una patente de la forma [A-Z]{4}[0-9]{3}
def ID_A_Patente(id: int) -> str:
    numero = int(str(id)[-3::]) - 1 if int(str(id)[-3::]) - 1 != -1 else 999
    potencias = id - numero
    potencias //= 1000
    indices = str(potencias)
    resultado = ""
    for i in indices:
        resultado += num_a_letras[int(i)] 
    resultado = resultado.rjust(4, "A") # Rellenamos con A's si es que el num era chico
    resultado += str(numero).rjust(3, "0") # appendeamos el numero de la patente (rellenando con 0s)
    return resultado

# Pruebas simples
assert(Patente_A_ID("AAAA000") == 1)
assert(Patente_A_ID("AAAB000") == 1001)
assert(Patente_A_ID("AABA023") == 10024)
assert(Patente_A_ID("AAAA999") == 1000)
ID_A_Patente(1001)
assert(ID_A_Patente(1) == "AAAA000")
assert(ID_A_Patente(1001) == "AAAB000")
assert(ID_A_Patente(10024) == "AABA023")
assert(ID_A_Patente(1000) == "AAAA999")