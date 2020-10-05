from random import randint

lst = [randint(10, 50) for _ in range(25)]
print(lst)

for i in range(len(lst) - 1):
    for j in range(len(lst) - 1 - i):
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst [j + 1], lst [j]

print(lst)


lst = [11, 13, 14, 14, 19, 20, 21, 22, 23, 28, 24, 28, 28, 28, 31, 31, 32, 35, 37, 40, 44, 44, 48, 48, 49]
print(lst)

def bubble_sort(my_list)
    cnt = 0
    for i in range(len(my_list) - 1):
        flag = True
        for j in range(len(my_list) - 1 - i):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
                flag = False
        cnt += 1
        if flag:
            break
    return cnt

print(lst)
print(cnt)