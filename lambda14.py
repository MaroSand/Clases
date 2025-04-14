lista = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

d = lambda x: x if len(x) == 6 else ""

dias_6 = list(filter(d, lista))

print(dias_6)