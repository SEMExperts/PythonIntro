template = '{surname:>13} {name[0]}.{average:>10.2}'

with open('src.txt', encoding='utf-8') as src, open('dst.txt', 'w', encoding='utf-8') as dst:
    for line in src:
        lst = line.strip('\n').split()
        grad = sum([int(grad) for grad in lst[2:]]) / len(lst[2:])
        res = template.format(
            surname=lst[1],
            name=lst[0],
            average=grad)
        dst.write(res)


if src.closed:
    print('File closed.')
