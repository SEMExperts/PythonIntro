from random import randint

lst = [randint(10, 99) for _ in range(15)]
print(lst)

key = 34
for i in range(len(lst)): # линейный поиск - перебор всех значений списка для того чтобы найти нужный
    if lst[i] == key:
        print(i)
        break

