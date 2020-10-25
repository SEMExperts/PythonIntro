"""
Написать функцию, которая принимает в качестве параметра целое, многозначное число.
Функция должна вернуть сумму произведений каждой цифры на её порядковый номер. Например:

есть число 874658734

8 имеет порядковый номер 1,
7 - 2
4 - 3
6 - 4
5 - 5 и т. д.
необходимо посчитать: 8 * 1 + 7 * 2 + 4 * 3 + 6 * 4 + 5 * 5 .....

Задачу надо решить с использование list comprehension и функции sum() в ОДНУ строку.
"""

num = 4895409804932580983245
s = str(num)
print(s)

lst = list(s)
print(lst)
l1 = [int(value) for value in lst]
print(l1)
# dict = dict(lst)
# print(dict)
# l1 = [int(value) for value in lst]
# print(l1)
# l2 = [value for value in l1]
# print(l2)

# l = [int(value)*(i+1) for value in lst for i in len(lst)]
# print(l)
print(len(lst))
for value in l1:
    print(value)

print(l1)
# s1 = [str(value) for value in l2]
# print(s1)
#
# m = ''.join(s1)
# print(m, type(m))
#
# num1 = int(m)
# print(num1, type(num1))