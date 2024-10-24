
def calcularmaxmin(lista_numeros):
    max = lista_numeros[0]
    min = lista_numeros[0]

    for numero in lista_numeros:
        if numero > max:
            max = numero     
        if numero < min:
            min = numero
    return max,min

Lista = []
while True: 
    num = int(input("ingrese un numero, cancela con 0: "))
    if num == 0: 
        break
    Lista.append(num)

maximo, minimo = calcularmaxmin(Lista)
print (f"el numero maximo es {maximo} y el minimo es {minimo}")





