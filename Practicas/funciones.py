#FUNCIONES
#Una funcion es un bloque de codigo que incluye instrucciones para realizar una tarea especifica


def saludar(nombre, edad):  #Definimos una funcion y sus parametros
    print(f"Hola {nombre}, tu edad es: {edad}")


saludar("Michel", 32) #Invocamos una funcion y enviamos los parametros


#FUNCIONES LAMBDA
# SOn funciones anoimas, que se ejecutan en una linea es decir pueden tener una expresion

resultado = lambda numero: numero + 20

print(f"El resultado es: {resultado(30)}")