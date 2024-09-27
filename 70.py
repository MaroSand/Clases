"""Un profesor necesita que escribamos un programa que lea las calificaciones de un parcial de los
alumnos de una clase (la cantidad de alumnos no es fija), luego de ingresar la nota del último
alumno se finaliza ingresando 0.
Las calificaciones se leen desde teclado y solo permiten números enteros entre 1 y 10. Utilizar lista.
Al ejecutar el programa debe solicitar el ingreso de las notas, y una vez finalizado el ingreso de las
notas, el programa deberá mostrara. Promedio de notas con dos decimales.
b. Cantidad de alumnos aprobados (que sacaron nota mayor o igual a 6)
c. Un histograma como el ejemplo, donde la cantidad de * indica la cantidad de veces que apareció
cada nota. Un histograma es un gráfico que muestra la frecuencia con que aparecen valores en un
conjunto dado."""

nota = 1
notas = []
cantnotas= 0
totalnotas= 0
aprobados = 0

while nota != 0:
    nota = int(input("ingrese nota: "))
    if nota == 0:
        break    
    elif nota > 10 or nota < 0:   
        print ("El numero ingresado es incorrecto")
        continue
    notas.append (nota)
    cantnotas += 1
    totalnotas += nota
    if nota >= 6:
        aprobados += 1

promedio = totalnotas / cantnotas
print(f"El promedio es: {promedio:.2f}")
print ((f"Aprobaron {aprobados} alumnos de {cantnotas} evaluados."))

cantidades= [0,0,0,0,0,0,0,0,0,0]

for i in notas:
    cantidades[i] += 1
    print(f"{i}: {'*' * cantidades}")

