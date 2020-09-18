"""
chr() - преобразовыввает код в символ
ord() -преобразовывает символ в код

"""

# 0x26bd
print(chr(0x26bd))
print('\u26bd')  # \u - 2байтный \U - 4х байтный символ
# &#9917;
print(chr(9917))

print(ord('⚽'))
print(hex(ord('⚽')))

wave = '~'
boat = '\U0001f6ac'
seagull = '\u033c'
fish = '\U0001f41f'
penguin = '\U0001f427'
wale = '\U0001f40b'
octopus = '\U0001f419'

seagull_row = wave * 11 + seagull + wave * 14 + '\n'
row = wave * 10 + boat + wave * 15 + '\n'
fish_row = wave * 4 + fish + wave * 21 + '\n'
wale_row = wave * 10 + wale + wave * 15 + '\n'
penguin_row = wave * 7 + penguin + wave * 18 + '\n'
octopus_row = wave * 17 + octopus + wave * 18 + '\n'

sea = seagull_row + row + fish_row + wale_row + penguin_row + octopus_row
print(sea)

# n1 = input('enter a num1: ')
# n2 = input('enter a num2: ')
# print(n1 + n2)
# print(int(n1) + int(n2))

s = 'Process finished with exit code 0'

#  0  1  2  3  4
#  H  E  L  L  O
# -5 -4 -3 -2 -1 - отрицательный индекс

print(s[0])
print(s[-1])

# s[0] = '7' ERROR
# print(s[35]) IndexError: string index out of range

# str[start: stop: step] - срез
print(s[8: 16: 1])
print(s[8: ])
print(s[: 16])
print(s[8: : 2])
print(s[8: 798237459234])
print(s[::-1])
print('12345'[::-1])

# len() - количество символов в строке
for i in range(0, len(s), 2):
    print(s[i], end='')
print()

#способы вывода символов
for symbol in s:
    print(symbol, end=' ')
print()

for i in range(len(s)):
    print(s[i], end=' ')
print()

# len(str)

# find(sub, start, end) - позволяет выполнить поиск вхождения строки в строку

print(len(s))
print(s.find('i'))

idx = s.find('i')
print(s.find('i', idx+1))

idx = s.find('i', idx+1)
print(idx)
idx = s.find('i', idx+1)
print(idx)
idx = s.find('i', idx+1)
print(idx)
idx = s.find('i', idx+1)
print(idx)
idx = s.find('i', idx+1)
print(idx)

# rfind(sub, start, end) - функция выполняет поиск символа справа-налево

#replace(old, new, count) - какое значение, в какой строке и сколько раз нужно заменить

print(s.replace('i', 'I'))
print(s.replace('i', 'I', 2))
print(s.replace('finished', 'finished'.upper()))

# count(str)
print(s.count('i'))

s = 'Process FINISHED with exit code 0'
# capitalize() - вывести строки с первой букве в верхнем регистре а остальные в нижнем
print(s.capitalize())

# upper()
# lower()

# title () - переводит все символы в нижний регистр кроме первых символов слов
print(s.title())

# strip(str) -

s = '       Hello  World!     '
print("'" + s + "'")
print("'" + s.strip() + "'")

s = '33333       Hello  World!     '
print("'" + s + "'")
print("'" + s.strip('3') + "'") #убирает тройки
print("'" + s.strip('3').strip() + "'") #убирает тройки и пробелы
s = 'Process         finished          with             exit            code 0'
# split() - позволяет разбить строку на части, по умолчанию на пробелы
# join() -
lst = s.split()
print(lst)
s= ' '.join(lst)
print(s)





