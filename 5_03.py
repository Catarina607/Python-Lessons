
import math

print('-----------------------------------')
print('   P  R  O G  R  A  M  M  I  N  G  ')
print('-----------------------------------')
n = int(input('Insert a number: '))


if n >= 0:
    y = math.sqrt(n)
    print(f' THE RESULT: √{n} = {int(y)}')
else:
    x = n**2
    print(f' {n}² = {x}')
