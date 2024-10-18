"""Escribir dos funciones que permitan calcular:
• La cantidad de segundos en un tiempo dado en horas, minutos y segundos.
• La cantidad de horas, minutos y segundos de un tiempo dado en segundos.
Escribe un programa principal con un menú donde se pueda elegir la opción de convertir a segundos,
convertir a horas,minutos y segundos o salir del programa.
"""

def HMS_a_seg(segundos):
   horas = segundos // 3600
   minutos = (segundos - (horas*3600)) //  60
   segs = (segundos-(horas*3600))-(minutos*60)
   print(f"{segs} segundos, en formato H:M:S es: {horas}:{minutos}:{segs}")
   

def segundos_a_HMS(H,M,S):
    segs = (H*3600)+(M*60)+S
    print(f"{H}:{M}:{S} son {segs} segundos.")
    

#MENÚ
while True:
    print("""Seleccione la opción deseada:
        1- Convertir horas y minutos a segundos.
        2- Convertir segundos a horas, minutos y segundos.: 
        3- Salir.""")
    opc = int(input("Ingrese su selección: "))
    
    if opc == 3:
        break
    elif opc == 1:
        segundos = int(input("Ingrese la cantidad de segundos: "))
        HMS_a_seg(segundos)
    elif opc == 2:
        horas= int(input("Ingrese la cantidad de horas: "))
        minutos = int(input("Ingrese la cantidad de minutos: "))
        segundos = int(input("Ingrese la cantidad de segundos: "))
        segundos_a_HMS(horas, minutos, segundos)
    else:
        print("Debe ingresar un valor correcto: 1, 2 o 3.")