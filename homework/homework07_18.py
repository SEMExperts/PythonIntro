"""
Даны два списка чисел. Посчитайте, сколько (уникальных) чисел содержится одновременно как в первом списке,
так и во втором.

  - Примечание. Эту задачу на Питоне можно решить в одну строчку.
"""

import random

a = int(input("Укажите длину первого списка: "))
b = int(input("Укажите длину второго списка: "))
lst1 = []
for _ in range(a):
    lst1.append(random.randint(0, 20))
lst2 = []
for _ in range(b):
    lst2.append(random.randint(0, 20))
print("Первый список: ", str(lst1))
print("Второй список: ", str(lst2))
print("Уникальные значения двух списков: ", str(set(lst1) & set(lst2)))
print("Кол-во уникальных значений двух списков: ", str(len(set(lst1) & set(lst2))))
