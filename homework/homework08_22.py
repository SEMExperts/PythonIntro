"""
Написать функцию is_year_leap, принимающую 1 аргумент — номер года, и возвращающую True,
если год високосный, и False иначе.
"""

def is_year_leap(y):
    if y / 4 == y // 4 and y / 100 != y // 100 or y / 400 == y // 400:
        return True
    else:
        return False

a = int(input('Введите год: '))
print('Год высокосный: ', is_year_leap(a))

