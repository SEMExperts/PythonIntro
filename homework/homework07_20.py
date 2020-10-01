"""
Дан текст (много строк в одном вводе) состоящий из нескольких строки.
Выведите слово, которое в этом тексте встречается чаще всего. Если таких слов несколько, выведите последнее.

Задачу необходимо решить с использованием словаря.
"""
from pprint import pprint

s = ("""How many cookies could a good cook cook, 
if a good cook could cook cookies? """)

lst = s.split()
print(lst)
d = dict()
max = 0
word = ''
for idx in range(0, len(lst)):
    x = 1
    if d.get(lst[idx]) != None:
        x = d.get(lst[idx]) + 1
        if max <= x:                # вводим доп условие чтобы определить слово которое встречается чаще всего
            max = x
            word = lst[idx]         # если условие верное то списку передастся значение этого слова
    d[lst[idx]] = x

print("Cколько раз встречается каждое слово: ")
pprint(d)
print("Слово, которое встречается чаще всего: ", word)

