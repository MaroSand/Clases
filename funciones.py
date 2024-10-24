a= int(input('Ingrese un número: '))
b= int(input('Ingrese un número: '))
f= input("Indique qué operación desea realizar (1.suma - 2.resta - 3. multiplicación - 4.divisón): ")

"""
def suma(a, b):
    return (a + b)

def resta(a, b):
    return (a - b)

def mult(a, b):
    return (a * b)

def div(a,b):
    return(a /b)


if f == '1':
    print(suma(a,b))
elif f == '2':
    print(resta(a, b))
elif f == '3':
    print(mult(a,b))
elif f == '4':
    print(div(a,b))
"""

def calculo(a,b):
    if f == '1':
        return(a+b)
    elif f == '2':
        return(a-b)
    elif f == '3':
        return(a*b)
    elif f == '4':
        return(a/b)
print(calculo(a,b))