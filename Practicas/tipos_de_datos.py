#en python existen 2 tipos de datos "NUMERICOS" y "CADENAS" aunque tambien podriamos decir que existen los boleanos

#NUMERICOS
# Enteros (int)
Entero = 10

# FLotantes (float)
flotante = 10.05

# Complejos (complex)
complejo = (10.05+0j)

# Boleanos (bool)
# Verdadero (True) y falso (False))
verdadero = True
falso = False

# CADENA DE TEXTO (str)
cadena = "Hola Michel, "
cadena2 = "Como estaS?"
cadenas_unidas = cadena + cadena2 # Concatenacion de cadenas
print(cadena)
print(cadena2)
print(cadenas_unidas)

Cadena_repetidas = "Hola " * 3 # Repeticion de cadenas
print(Cadena_repetidas)


# Operadores de permanencia
#Estos operadores evaluan si un objeto se encuentra dentro de otro
#  in - se encuentra en
#  not int - No se encuentra en

cadena = "MichelVelasco"
print('v' not in cadena)

# Operadores de identidad
# Nos permiten comprobar si un objeto es igual o no a otro objeto
#  is y is not

a = 10
b = 10

print(type(a) is not str)