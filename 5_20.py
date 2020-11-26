
import math

a = float(input('Write the side [A] of the Triangle m: '))
b = float(input('Write the side [B] of the Triangle m: '))
c = float(input('Write the side [C] of the Triangle m: '))

a_measure = a**2
b_measure = b**2
c_measure = b**2

tri_area = int(math.sqrt(a_measure+b_measure+c_measure))
print(f'The triangle area is equal {tri_area} m²')


if a == b and b == a and b == c and c == a:
    print('This Triangle is EQUILATERAL')
elif a != b and b == c:
    print('This Triangle is ISOSCELES')
elif a != c and c == b:
    print('This Triangle is ISOSCELES')
elif a == c and a!= b and c!= b:
    print('This Triangle is ISOSCELES')
elif a != b and b != a and c != a and c != b:
    print('This Triangle is SCALENE')
else:
    print('=============================')

