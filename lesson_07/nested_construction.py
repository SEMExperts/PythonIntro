cols = 11
rows = 11

for i in range(rows):
    for j in range(cols):
        print('\u26bd', end=' ')
    print()  # переход на новую строку

for i in range(rows):
    for j in range(cols):
        if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
            print('*  ', end='')
        else:
            print('   ', end='')
    print()  # переход на новую строку

for i in range(rows):
    for j in range(cols):
        if i == 0 or i == rows - 1 or j == 0 or j == cols - 1 or i == j:
            print('*  ', end='')
        else:
            print('   ', end='')
    print()  # переход на новую строку

for i in range(rows):
    for j in range(cols):
        if i == 0 or i == rows - 1 or j == 0 or j == cols - 1 or i == j or j == cols - 1 - i or j == cols // 2:
            print('*  ', end='')
        else:
            print('   ', end='')
    print()  # переход на новую строку

for i in range(rows):
    for j in range(cols):
        if (i == 0 or
                i == rows - 1 or
                j == 0 or
                j == cols - 1 or
                i == j or
                j == cols - 1 - i or
                j == cols // 2 or
                i == rows // 2):
            print('*  ', end='')
        else:
            print('   ', end='')
    print()  # переход на новую строку
