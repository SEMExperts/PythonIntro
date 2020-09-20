# a = []  # созает список
# print(a, type(a))
# a = list() # созает список
# print(a, type(a))
#
# a = list('Hello World!')
# print(a, type(a))
#
# a = list(21313141325) # не допустимая операция - отдает ошибку
# print(a, type(a))
#
#
# a = list(str(21313141325))
# print(a, type(a))

a = [1, 5, 7, 8, 6]
print(a, type(a))

a = [1, 'jlkj;lkj', 78.76, True, 6]
print(a, type(a))

print(a[3])  # обращение по индексу

a = list('Hello World!')
print(a[2: -2: 2])  # срез
print(a[::-1])  # перевернутый списко

for i in range(len(a)):
    print(a[i], end='')
print()

for element in a:
    print(element, end='')
print()

for idx, element in enumerate(a, 1):  # в скобках с какого элемента списка начинать
    print(idx, element)

a1 = [1, 2, 3, 4, 5]
b1 = [6, 7, 8, 9, 0]
c1 = a1 + b1
print(c1)

c2 = a1 * 4
print(c2)

# len(lst) - кол-во элементов в списке
print(len(c2))

print(a1)
a1.append(45)  # позволяет добавить элемент в конец списка
print(a1)

del a1[2]  # удаляет элемент из списка
print(a1)

# del a1 # удаляет весь списко и выдает ошибку при обращении
# print(a1)

x = a1.pop(1)  # функция удаляет элемент и возвращает в переменную
print(x, a1)

# count(value)
a1 = a1 * 3
print(a1.count(5))  # можно определить кол-во элементов в списке

a1 = [1, 2, 3, 4, 5]
b1 = [6, 7, 8, 9, 0]
c1 = a1 + b1
print(a1, b1)
print(c1)

a1.extend(b1)  # расширить список добавив в него элементы вторго списка
print(a1)

print(a1.index(5)) # позволяет получить индекс элемента по значению


# a1.insert()  # позволяет добавить нужное значение в нужную позицию  insert(idx, value)

print(a1)
a1.insert(5, 99)
print(a1)

# a1.remove() # удаляет значение из списка, при передачи не существующего получаем ошибку
a1.remove(99)
print(a1)

a1.reverse() # переворачивает существующий список и при этом список не меняется
print(a1)


# in позволяет получить ответ true или false на запрашиваемое значение

print(a1)
print(5 in a1)
print(a1)



