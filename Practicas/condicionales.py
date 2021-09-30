
def mayor_numero(n1, n2, n3):
    if n1 >= n2	and n1 >=n3:
        return n1
    if n2 >= n1 and n2 >= n3:
        return n2
    else:
        return n3

numero = mayor_numero(99, 556, 300)
print(numero)