m = lambda x: x['color']

lista = [
    {'make': 'Nokia', 'model': 216, 'color': 'Black'},
    {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
    ]

lista_ordenada = sorted(lista, key= m)
print(lista_ordenada)