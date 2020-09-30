"""
Дан список из чисел и индекс элемента в списке `k`. Удалите из списка элемент с индексом `k`,
сдвинув влево все элементы, стоящие правее элемента с индексом `k`.

  Программа получает на вход список (список можно создать и заполнить случайными числами), затем число `k`.
  Программа сдвигает все элементы, а после этого удаляет последний элемент списка при помощи метода `pop()`
  (да, такой метод есть в арсенале списков. Я ошибочно сказал, что его нет. pop() без параметра,
  удаляет последний элемент списка и возвращает его значение) без параметров.
Программа должна осуществлять сдвиг непосредственно в списке. Также нельзя использовать дополнительный список.
Также не следует использовать метод `pop(k)` с параметром.
Использовать оператор del НЕЛЬЗЯ!
"""
import random

r = int(input("Укажите длину списка: "))
s = []
for _ in range(r):
    s.append(random.randint(0, 200))
print(s)
k = int(input("Укажите элемент для удаления: "))
x = 0
for idx in range(r-1):
    s[idx] = s[x]
    x += 1
    if s[idx+1] == k:
        x += 1

s.pop()
print(s)