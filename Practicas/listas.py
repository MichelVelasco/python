# LISTAS
#Las listas son una collecion de elementos, las listas estan ordenadas y son mutables
numeros = [5, 2, 23, 55, 1, 9, 6]
frutas = ["Naranja", "Manzana","Kiwi", "Mandarina", "Uva", "Fresa"]

#print (frutas)
#print(frutas[4])
#print(frutas[-6])
#print(frutas[1:5])

#FUNCIONES DE LAS LISTAS
# list, len, append, extend, insert, remove, clear, pop, index, count, sort, reverse, copy
frutas.append("Piña")
print(len(frutas))
lista2 = numeros + frutas
print(lista2)
#numeros.extend(frutas)
print(numeros)
frutas.insert(2,"Banana")
frutas.remove("Kiwi")
print(frutas.index("Fresa"))
frutas.sort()
print(frutas)
numeros.reverse()
print(numeros)

