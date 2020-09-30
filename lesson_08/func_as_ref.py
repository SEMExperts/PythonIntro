from random import randint

lst = [randint(10, 50) for _ in range(10)]
print(lst)

def func(my_lst):
    for i in range(len(my_lst)-1):
        if my_lst[i] < my_lst[i+1]:
            print('<')
        elif my_lst[i] > my_lst[i+1]:
            print('>')
        else:
            print('=')


print(func(lst))