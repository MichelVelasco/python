#Calculadora 2.0

num1 = float (input("Ingresa un numero: "))
operador = input("Ingresa un operador: ")
num2 = float (input("Ingresa otro numero: "))

if operador == "+":
    res = num1 + num2
    print("La suma es: " + str (res))
elif operador == "-":
    res = num1 - num2
    print("La resta es: " + str(res))
elif operador == "*":
    res = num1 * num2
    print("La multiplicaion es: " + str(res))
elif operador == "/":
    res = num1 + num2
    print("La division es: " + str(res))
