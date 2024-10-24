"""Desarrolle un programa que permita cargar los nombres y notas de n alumnos (dejando de
ingresar datos cuando se ingrese un nombre en blanco). Los nombres se deben cargar en una lista
y las notas de otra. Las notas solo deben permitir número enteros entre 1 y 10.
Una vez cargados ñps datos, debe mostrar el sgte menú:
MENU DE OPCIONES
----------------
1-Porcentaje de alumnos aprobados.
2 Promedio de notas
3-Listado de nombres y nota de los alumnos desaprobados.
0- Salir
Ingrese la opciòn:
Realizar la función para cada opción que deben realizar lo siguiente()"""

nombres = []
notas = []

def porcentaje(lista_notas):
    total = 0
    aprobados = 0
    for i in lista_notas:
        total += 1
        if i >= 6:
            aprobados += 1
    porcentaje = (aprobados/total) * 100
    return porcentaje
        
def promedio(lista_notas):
    suma = 0
    cant_alumnos = 0
    for i in lista_notas:
        suma += i
        cant_alumnos += 1
    promedio = suma/cant_alumnos
    return promedio

def desaprobados(lista_nombres, lista_notas):
    cantidad = 0
    for i in lista_notas:
        cantidad += 1
    print("Los alumnos desaprobados son: ")
    for i in range(cantidad):
        if lista_notas[i] < 6:
            print(f"Lista de desaprobados: {lista_nombres[i]}:{lista_notas[i]}")



while True:
    nombre = input("Ingrese el nombre: ")
    if nombre == "":
        break
    nombres.append(nombre)

    while True:
        nota= int(input(f"Ingrese la nota de {nombre}: "))
        if nota in range(1,11):
            break
        else:
            print("Valor incorrecto Ingrese enteros entre 1 y 10.")
    notas.append(nota)

print(nombres)
print(notas)

while True:
    print("""MENU DE OPCIONES
----------------
1-Porcentaje de alumnos aprobados.
2-Promedio de notas
3-Listado de nombres y nota de los alumnos desaprobados.
0-Salir""")
    opc = int(input("Ingrese la opción: "))
    if opc == 0:
        print("Hasta luego.")
        break
    elif opc == 1:
        print("El porcentaje de alumnos aprobados es:", porcentaje(notas),"%")
    elif opc == 2:
        print("El promedio de notas es:",promedio(notas))
    elif opc == 3:
        desaprobados(nombres, notas)
    else:
        print("Ingrese un valor correcto.")