"""Дана строка, состоящая из слов, разделенных пробелами. Определите, сколько в ней слов.
Используйте для решения задачи функцию `count()`
"""
s = input() # ввод текста
lst = s.split() # разбиваем строку на части
s = ' '.join(lst) # соединяем в цельную строку с проблеами межуд словами
print(s.count(' ') + 1)
