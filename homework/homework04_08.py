"""
По данному натуральному числу N найдите наибольшую целую степень двойки, не превосходящую N.
Выведите показатель степени и саму степень. Операцию возведения в степень,
а так же функцию возведения в степень использоваться НЕЛЬЗЯ!

Например:
50     5 32      2 ** 5 = 32
10     3 8       2 ** 3 = 8
8      3 8       2 ** 3 = 8
7      2 4       2 ** 2 = 4
1      0 1       2 ** 0 = 1
2      1 2       2 ** 1 = 2
3      1 2       2 ** 1 = 2
4      2 4       2 ** 2 = 4
5      2 4       2 ** 2 = 4
100     6 64      2 ** 6 = 64
1025    10 1024     2 ** 10 = 1024
15431543  23 8388608   2 ** 23 = 8388608
"""

N = int(input('Введите натуральное число: '))
i = 1
while True:
    if N < 2 ** i:
        print(str(i - 1) + ' ' + str(2 ** (i - 1)))
        break

    i += 1