# ADIVINA EL NUMERO 1.0

import random

adivina = random.randint(1, 10)

print("Hola, cual es tu nombre? ")
nombre = input()

print("Muy bien " + nombre + " estoy pensando un numero entre 1 y 10, intenta adivinarlo")
print("Recuerda que solo tienes 3 intentos")

num = int (input("Ingresa un numero: "))

if num == adivina:
    print("GANASTE!")
else:
    if num > adivina:
        print("Intenta con un numero mas pequeño")
    else:
        print("Intenta con un numero mas grande")
    print("\n Te quedan 2 intentos")

num = int (input("Ingresa un numero: "))

if num == adivina:
    print("GANASTE!")
else:
    if num > adivina:
        print("Intenta con un numero mas pequeño")
    else:
        print("Intenta con un numero mas grande")
    print("\n Te quedan 1 intentos")

num = int (input("Ingresa un numero: "))

if num == adivina:
    print("GANASTE!")
else:
    print("PERDISTE")