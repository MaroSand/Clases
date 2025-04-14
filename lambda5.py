par = lambda x : (x % 2 == 0)

imp = lambda x : (x % 2 != 0)

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_pares = list(filter(par,lista))
lista_impares =list(filter(imp, lista))

print("Lista original:", lista)
print("Lista números pares: ", lista_pares)
print("Lista números impares: ", lista_impares)