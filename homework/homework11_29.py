cols = 11
rows = 11
#
# for i in range(rows):
#     for j in range(cols):
#         if (
#                 # i == 0 or   # верхняя горизонтальная линия
#                 # i == rows - 1 # нижняя горизонтальная линия
#                 # j == 0 or  #левая сторона
#                 # j == cols - 1 or # правая сторона
#                 # i == j or  # диагональ с левого верхнего угла
#                 # j == cols - 1 - i or # диагональ с правого верхнего угла
#                 # j == cols // 2 or   # вертикальная линия по центру
#                 # i == rows // 2
#         ):
#             print('*  ', end='')
#         else:
#             print('   ', end='')
#     print()  # переход на новую строку
#

# for i in range(rows):
#     for j in range(rows * 2 - 1):
#         if (j - i == (rows * 2 - 1) // 2 or
#                 j == (rows * 2 - 1) // 2 - i or
#                 i == rows - 1
#
#         ):
#             print('*  ', end='')
#         else:
#             print('   ', end='')
#     print()  # переход на новую строку
# print()

c = rows -1
print(c)
for i in range(rows):
    for j in range(rows * 2 - 1):
        if (
            # j - i == (rows * 2 - 1) // 2 or
            # j == (rows * 2 - 1) // 2 - i or
            i == rows - 1 or
            # j == (rows * 2 - 1) // 2 or
            j == c  or
            j == c + i or
            j == c - i or
            j + 1 == c + i and j + 1 != c or
            j + 2 == c + i and j + 1 != c and j + 2 != c or
            j + 3 == c + i and j + 1 != c and j + 2 != c and j + 3 != c or
            j + 4 == c + i and j + 1 != c and j + 2 != c and j + 3 != c and j + 4 != c
        ):
            print('*  ', end='')
        else:
            print('   ', end='')
    print()  # переход на новую строку
