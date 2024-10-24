palabra1= str(input("Ingrese una palabra: "))
palabra2 = str(input("Ingrese otra palabra: "))

if len(palabra1) > len(palabra2) :
    print("La palabra ",palabra1," es más larga que ",palabra2)
elif len(palabra1)==len(palabra2):
    print("Las dos palabras tienen la misma cantidad de caractéres")
else:
    print("La palabra ",palabra2," es mayor que ",palabra1)