def konv(n, s):
    b = ''
    while n > 0:
        b = str(n % s) + b
        n = n // s
    return b


n = int(input("Введите число: "))
s = int(input("Введите систему исчисления: "))

print(konv(n,s))
