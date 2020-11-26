
print('==================================')
print('   L E A P  Y E A R  R E A D E R  ')
print('===================================')

year = int(input('YYYY: '))
y_c1 = year%4
if y_c1 == 0 and year % 100 > 0:
    print('It is a Leap Year.')
else:
    print('It Isnt a Leap Year.')
