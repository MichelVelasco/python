#TRABAJANDO CON CADENAS DE TEXTO

# Las cadenas pueden tratarse como listas

cadena = "Hola Michel Velasco"
# H O L A     M I C H E L      V   E  L  A  S  C  O
# 0 1 2 3  4  5 6 7 8 9 10  11  12  13 14 15 16 17 18 1

letra = cadena[5]
print(letra)

letra = cadena[-1]
print(letra)

letras = cadena[5:11]
print(letras)

# FUNCIONES DE LAS CADENAS DE TEXTO
# 

cadena2 = cadena.split()
print(cadena2)

cadena_con_comas = "Luis,Michel,Velasco,Gonzalez"
listaNombre = cadena_con_comas.split(',')

# UNIENDO VARIABLES y CADENA
alumnos =2500
escuela = "UdeG"
cadena = "Los " + str(alumnos) + " alumnos de " + escuela  #Concatenacion cambiando el tipo de variable int a str 
print(cadena)

# .format
cadena = "Los {} alimnos de la {}".format(alumnos, escuela) # recibimos es parametros y los enviamos a donde queremos imprimirlos 
print(cadena)
cadena = "Los {a} alimnos de la {b}".format(a = alumnos, b= escuela)
print(cadena)

cadena = f"Los {alumnos} alumnos de la {escuela}"
print(cadena)

#INTRODUCIR TEXTO POR TECLADO
#la funcion de python que nos permite introducir texto es input()

print("Ingresa tu nombre")
nombre = input()
print(nombre)
nombre = input("Ingresa tu nombre: ")
print(f"Hola {nombre} ")
