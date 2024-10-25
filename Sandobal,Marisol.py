fechas = []
temperaturas = []
momentos = []

def promedio(lista_temp):
    suma = 0
    cantidad = 0
    for i in lista_temp:
        suma += i
        cantidad += 1
    promedio = suma / cantidad
    print(f"El promedio de temperaturas es {promedio:.2f}ºC.")
    

def menorTemperatura(lista_fechas, lista_temp, lista_momomentos):
    menor_temp = lista_temp[0]
    cantidad = 0

    for i in lista_temp:
        cantidad += 1
        if i < menor_temp:
            menor_temp = i
    print(f"Momento de temperatura más baja")
    for i in range(cantidad):
        if lista_temp[i] == menor_temp:
            print(f"Menor temperatura: {lista_fechas[i]} {lista_momentos[i]} ")

def observ_tarde(lista_fecha, lista_temp, lista_momentos):
    for i in lista_momentos:
        if i == T:
            print(f"Observaciones a la tarde {lista_fecha[i]}  {lista_momentos[i]}")

long_fecha = 0
while True:
    fecha = int(input("Ingrese la fecha sin guiones ni espacios (Sale con Enter): "))
    if fecha == "":
        break
    if fecha == 8:
        long_fecha += 1
        fechas.append(fecha)
    else:
        print("Valor inválido. Ingrese 8 dígitos")


    while True:
        temperatura= float(input("Ingrese la temperatura: "))
        break
    temperaturas.append(temperatura)

    while True:
        momento = input("Ingrese 'M' (Mañana) - 'T' (Tarde) - 'N' (Noche): ")
        if momento == 'M' or momento == 'T' or momento == 'N':
            momentos.append(momento)
        else:
            print("Ingreso de dato incorrecto. Vuelva a intentar.")


print(fechas)
print(temperaturas)
print(momentos)

while True:
    print("""MENÚ
    ----
    1.Promedio de todas las temperaturas con dos decimales.
    2.Fecha y momento de la menor temperatura registrada.
    3.Mostrar un listado de fecha y temperatura, de las observaciones que se hicieron a la tarde.
    0.Salir""")
    opc = int(input("Ingrese la opción: "))

    if opc == 0:
        print("Hasta luego.")
        break
    elif opc == 1:
        promedio(temperaturas)
    elif opc == 2:
        menorTemperatura(fechas, temperaturas, momentos)
    elif opc == 3:
        observ_tarde(fechas, temperaturas, momentos)
    else:
        print("Ingrese un valor correcto.")