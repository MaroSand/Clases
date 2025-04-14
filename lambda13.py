#Even/Odd Count Lambda

lista = [1, 2, 3, 5, 7, 8, 9, 10]

par= lambda x: x%2==0
impar = lambda x: x%2!=0

pa = list(filter(par, lista))
imp = list(filter(impar, lista))

print("Cantidad de números pares:", len(pa))
print("Cantidad de números impares:", len(imp))