"""Escribir un programa que introduzca el número de un mes (1 a 12) y visualice el número de días
de ese mes."""
import calendar

def dias_en_el_mes(mes,año):
    return calendar.monthrange(año,mes)[1]

mes = int(input("Introduzca un numero de mes: "))
año = int(input("Ingrese el año: "))

meses = ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]

valor_mes = meses[mes - 1]

if 1 <= mes <= 12:
    dia = dias_en_el_mes(mes,año) 
    print(f" el mes de {valor_mes} del año {año} tiene {dia} dias en el mes")
else:
    print ("el numero ingresado es incorrecto")
