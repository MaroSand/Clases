"""
Escriba un programa que pida al usuario la entrada correspondiente y calcule el factorial n! de
un número entero n≥0, definido como:
n!=1⋅2⋅3⋅⋯⋅n.
Además, se define 0!=1
"""

num= int(input("Ingrese un número: "))

factorial = 1
"""
for i in range (1,num + 1):
    factorial = num * (i+1)
"""

for i in range(1, num + 1):

    factorial *= i
    
    print(f"{factorial}")
