"""
Пользователь вводит, отдельно, строку `s` и один символ `ch`. Необходимо выполнить поиск в строке `s` всех символов `ch`.

Для решения НУЖНО использовать только функцию `find()`(rfind()), операторы `if` и `for`(while).
"""

s = input()
ch = input()
print(len(s))
for i in range(0, len(s)):
    print(i)
    # if s.find(ch, i, +i) == TRUE:
    #     print(s.find(ch, i))
