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

def Patente_A_ID(patente: str) -> int:
    letras = patente[0:4]
    numeros = int(patente[4::])
    ID = 0

    for i, letra in enumerate(reversed(letras)):
        ID += letras_a_num[letra]*(10**(i+3))
    ID += numeros + 1

    return ID

def ID_A_Patente(id: int) -> str:
    numero = int(str(id)[-4::]) - 1
    letras = str(id)[0:-4]
    print(letras)
    pass

# Pruebas simples
assert(Patente_A_ID("AAAA000") == 1)
assert(Patente_A_ID("AAAB000") == 1001)
assert(Patente_A_ID("AABA023") == 10024)
assert(Patente_A_ID("AAAA999") == 1000)

ID_A_Patente(10024)


# assert(ID_A_Patente(1) == "AAAA000")
# assert(ID_A_Patente(1001) == "AAAB000")
# assert(ID_A_Patente(10024) == "AABA023")