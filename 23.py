""""
 Hacer un algoritmo que analice si en dos números ingresados: cual es mayor, cual es menor, o si
son iguales
"""

num1 = float(input("Ingrese un número: "))
num2 = float(input("Ingrese un número: "))

if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num1 < num2:
        print(f"{num1} es menor que {num2}")
else:
      print("Ambos números son iguales.")
    