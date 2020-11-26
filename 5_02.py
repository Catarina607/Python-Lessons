

import math

print('-------------------------------------')
print('    P  R  O  G  R  A  M  M  I  N  G  ')
print('-------------------------------------')
n = int(input('Insert a number: '))


if n > 0:
    nsqrt = math.sqrt(n)
    print(f'The Square root of it is about {int(nsqrt)}')
else:
    print('INVALID NUMBER')
