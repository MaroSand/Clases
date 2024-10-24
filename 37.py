"""Desarrolle un programa para estimar el valor de π usando la siguiente suma infinita:
π=4*(1−1/3+1/5−1/7+…)
La entrada del programa debe ser un número entero n que indique cuántos términos de la suma se
utilizará.
n: 3            3.466666666666667       n: 1000    3.140592653839794"""

numero = int(input("ingrese la cantidad de terminos: "))
suma = 0
signo = 1
for i in range (1,2*numero,2):
    suma = suma + (1/i) * signo
    signo = signo * -1
pi = 4 * suma
print (f"el valor estimado de pi con {numero} terminos es {pi}")
print (f"la diferencia es {3.140592653839794 - pi}")