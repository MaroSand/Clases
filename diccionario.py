#Se crean con llaves
"""
cartera = dict()
cartera['dolares'] = 5
cartera['labiales'] = 8
cartera['papeles'] = 5
print(cartera)

ddd = dict()
ddd['edad'] = 21
ddd['curso'] = 182
print(ddd)


ddd['edad'] = 23
print(ddd)

___

jjj = {'Carlos' : 1 , 'Alfredo': 2}
print(jjj)

___

contadores = dict()
nombres = ['Sergio', 'Carlos', 'Sergio', 'Saúl', 'Carlos']
for nombre in nombres:
    if nombre in contadores:
        contadores[nombre] = contadores[nombre] + 1
    else:
        contadores[nombre] = 1
print(contadores)

____


contadores = dict()
cant_letras= dict()
#len(palabra) devuelve la cantidad de letras que tiene la palabra
print('Ingresa una línea de texto: ')
lineaa = input('')

palabras = lineaa.split()

print('Palabras:', palabras)

print('Contando...')
for palabra in palabras:
    #contadores[palabra]= contadores.get(palabra,0)+ 1
    if palabra in contadores:
        contadores[palabra] = contadores[palabra] + 1
    else:
        contadores[palabra] = 1
        cant_letras[palabra] = len(palabra)

print('Contadores', contadores)
print("Cantidad de letras:", cant_letras)

___

"""
nombre = input('Ingresa un nombre de archivo: ')
archivo = open(nombre)

contadors = dict()
for linea in archivo:
    palabras = linea.split()
    for palabra in palabras:
        contadores[palabra] = contadores.get(palabras,0) + 1

grancontador = None
granpalabra = None
for palabra, contador in contadores.items():
    if grancontador is ÇNone or contador > grancontador:
        granpalabra = palabragrancontador = contador

print(granpalabra, grancontador)