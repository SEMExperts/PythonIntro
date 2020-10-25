import random

"""
if condition:
    value = expression_1
else:
    value = expression_2


            1          |    2       |   3
value = expression_1 if condition else expression_2     # тернарный оператор ПРОЯСНИТЬ
"""

#               1       |       2       |       3
# new_lst = [expression for element in collection filter]

lst1 = [value for value in range(10, 21)]
print(lst1)

lst2 = [value for value in range(100) if value % 2]
print(lst2)
"""
random.random()                     # вещественные значение от 0 до 1 
random.randint(start, stop)         # генерирует значение от start до stop
random.uniform(start, stop)         # генерирует вещественные случайные числа от старт до стоп
random.randrange(start, stop, step) # случайные числа в диапазоне
"""

# for _ in range(10):
#     print(random.random(), end=',')
# print()
#
# for _ in range(10):
#     print(random.randint(1, 50), end=',')
# print()
#
# for _ in range(10):
#     print(random.uniform(0.1, 9.9), end=',')
# print()
#
# for _ in range(10):
#     print(random.randrange(10, 20, 2), end=',')
# print()

# lst3 = [random.randint(1, 100) for _ in range(20)]
# print(lst3)

num = 4895409804932580983245
s = str(num)
print(s)
lst = list(s)
print(lst)
l1 = [int(value) for value in lst]
print(l1)
l2 = [value * 2 for value in l1]
print(l2)
s1 = [str(value) for value in l2]
print(s1)
m = ''.join(s1)
print(m, type(m))
num1 = int(m)
print(num1, type(num1))

num2 = int(''.join([str(int(value) * 2) for value in str(num)]))  # заменяет все написанное выше
print(num2, type(num2))

s = 'lower case string'  # lOwEr CaSe StRiNg
# l = ''.join([el.upper() if])
