"""
Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12),
 и возвращающую время года (в виде строки), которому этот месяц принадлежит (зима, весна, лето или осень).
"""

def season(m):
    if m == 12 or m == 1 or m == 2:
        return 'зима'
    elif m == 3 or m == 4 or m == 5:
        return 'весна'
    elif m == 6 or m == 7 or m == 8:
        return 'лето'
    elif m == 9 or m == 10 or m == 11:
        return 'осень'
    else:
        return 'нет такого месяца'

m = int(input('Введите номер месяца: '))
print(season(m))