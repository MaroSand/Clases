"""Crea una función “calcularMaxMin” que recibe una lista con valores numéricos y devuelve el valor
máximo y el mínimo. Crea un programa que pida números por teclado y muestre el máximo y el
mínimo, sin utilizar los métodos de listas.
"""

def calcularmaxmin(lista_numeros):
    max = lista_numeros[0]
    min = lista_numeros[0]

    for numero in lista_numeros:
        if numero > max:
            max = numero
        
        if numero < min:
            min = numero

    return max, min

lista = []
while True:
    num = int(input("Ingrese un número, sale con 0: "))
    if num == 0:
        break
    lista.append(num)

maximo, minimo = calcularmaxmin(lista)

print(lista)
print(f"El máximo es {maximo} y el mínimo es {minimo}.")