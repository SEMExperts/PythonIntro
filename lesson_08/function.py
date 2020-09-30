# """
# def name_function(param1,param2, ... paramN):
#     function body
#
# expression
# """
#
#
# def print_hello():
#     print('Hello World!')
#
#
# print_hello()
#
#
# def print_text(text):
#     print(text)
#
#
# print_text('Привет народ')
#
#
# def my_pow(num, exp):
#     res = num ** exp
#     return res
#
#
# a = int(input('Please enter a number: '))
# b = int(input('Please enter exp: '))
# x = my_pow(2, 6)
# print(x)
#
# x = my_pow(3 * a, b - 2)
# print(x)

# x = 5  # переменная называется глобальной
#
#
# def func():
#     f = 0  # локальные переменные
#     global x
#     x = 12
#     print(x)
#
#
# def my_pow(num, exp=2):  # внесен аргумент по умолчанию. они должны быть вконце списка
#     print(num ** exp)
#
#
# my_pow(3, 5)
# my_pow(3)
#
#
# def func(a, b, c, d=12, e=22, f=32):
#     print(a, b, c, d, e, f)
#
#
# func(1, 2, 3)
# func(1, 2, 3, 42, 52)
#
# func(1, 2, 3, f=56)  # обращение к аргументу по имени
#
#
# def func(a, b[]):
#     print(a, b)
#     b.append(a)
#     print(a, b)
#
# func(1)
#
#
# def func1(*args):                   #список неименованных (кортеж)
#     print(type(args), args)
#     for value in args:
#         print(value)
#
#
# func1(1,2,3,4)
#
#
# def func2(**kwargs):                #список именованных аргументов (словарь)
#     print(type(kwargs), kwargs)
#
#
# func2(a=1, b=3, g=7)


