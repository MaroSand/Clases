#Array Intersection Lambda

a = [1, 2, 3, 5, 7, 8, 9, 10]
b = [1, 2, 4, 8, 9]

array = list(filter(lambda x: x in a,b))

print("Intersección de números: ", array)