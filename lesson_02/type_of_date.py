# вещественный тип
print(4.7)
print(0.1 + 0.1 + 0.1)

a = 3 ** 10000
print(a)
# print(a + 0.1)
# 2.23 * 10 ^ -308 1.79 *10^308 максимальные значения
# 2.23e-308   1.79e308
# ing -inf бесконеность
# nan


# комплексные числа
print(2 + 3j, type(2 + 3j))

# string
r = 'asdfasdfasdfasdlkfjsaldjf'
s1 = 'Hello '
s2 = 'World!'
s3 = s1 + s2
print(s3)
s4 = s1 * 5
print(s4)

# ESCAPE
"""
\n  new line
\t  tab
\b  backspace
\'  '
\"
\\  \
\a  alarm - ascii bell
"""

t1 = 'Hello \'World\'!'
print(t1)
t2 = 'Hello World!'
t3 = '\\'
print(t3)
t4 = '\a'
print(t4)

# text
u = '''
asdfasdf;lj;lkjlj
ljasdlfj
lkajdlfkj
\lajsdflkj
asdf

asdfkkl
'''
print(u)