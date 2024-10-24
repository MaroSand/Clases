"""
Hacer un algoritmo que permita ingresar N números y que luego calcule la suma y el promedio
de los números ingresados.
"""
number=1
sum = 0
cant_numbers=0

while number != 0:

    number = float(input("Ingrese un número por favor: "))
    
    if number != 0:
        cant_numbers+=1
        
    sum += number

promedio = sum / cant_numbers


print("El promedio de los numeros ingresados es: ",promedio,)
print("Cantidad de números ingresados es: ",cant_numbers)

