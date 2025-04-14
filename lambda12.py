lista = [-1, 2, -3, 5, 7, 8, 9, -10]

print(sorted(lista, key = lambda x: 0 if x == 0 else -1/x))