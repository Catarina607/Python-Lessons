
print('==================================')
print('         MATHEMATICS PROOF        ')
print('==================================')
a = int(input('2 + 5 = '))
b = int(input('4 + 5 = '))
c = int(input('5 + 5 = '))
d = int(input('7 + 4 = '))
e = int(input('2 + 9 = '))


if a == 7:
    a = 1
    print('a) Right!')
else:
    a = 0
    print('a) Wrong!')


if b == 9:
    b = 1
    print('b) Right!')
else:
    b = 0
    print('b) Wrong')


if c == 10:
    c = 1
    print('c) Right!')
else:
    c = 0
    print('c) Wrong!')


if d == 11:
    y = 1
    print('d) Right!')
else:
    y = 0
    print('d) Wrong!')


if e == 11:
    e = 1
    print('e) Right!')
else:
    e = 0
    print('e) Wrong!')


q = a + b + c + y + e
print('Correct Question: ',  q)
