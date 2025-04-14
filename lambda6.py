#Square & Cube Lambda

cuadrado = lambda x : (x**2)

cubo = lambda x : (x**3)

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_cuadrados = list(map(cuadrado, lista))

lista_cubo = list(map(cubo, lista))

print("Números: ", lista)
print("Números al cuadrado: ",lista_cuadrados)
print("Números al cubo: ", lista_cubo)