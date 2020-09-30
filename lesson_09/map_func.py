# map(func_ref, collection)
temperatures = (36.5, 37, 37.5, 38)
F1 = list(map(lambda t: round(((float(9)/5*t) + 32), 2), temperatures))
print(F1)
C1 = list(map(lambda t: round((float(5)/9)*(t-32), 2), F1))
print(C1)

S = list( , lst)