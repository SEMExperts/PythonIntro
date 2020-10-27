from pprint import pprint

with open('src.txt', encoding='utf-8') as file, open('result.txt', 'w', encoding='utf-8') as res:
    mid = 0
    for line in file:
        lst = line.strip('\n').split()
        name = (lst[1] + ' ' + lst[0][0] + '. ')
        avr = 0
        for i in range(2, len(lst)):
            avr += int(lst[i])
        avr = avr / (len(lst[2:]))
        mid += avr
        s = (name + str(round(avr, 2))+ '\n')
        res.write(s)
        if avr < 5:
            print(name, round(avr, 2))
    print('Средний балл: ', round(mid / len(lst[2:]), 2))
