"""
Дана строка. Замените в этой строке все появления буквы `h` на букву `H`, кроме первого и последнего вхождения.

Понадобятся: срезы, функция replace().
"""
s = input()
s1 = s.find('h') + 1 # находим первое вхождение, добавляем 1 так как следующий символ будет местом "отсечки" в строке
s2 = s.rfind('h') # находи последниее вхождение
print(s[:s1] + s[s1:s2].replace('h', 'H') + s[s2:])
