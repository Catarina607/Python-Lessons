
print('===========================================')
print('  G A S O L I N E   C O N S U M P T I O N ')
print('===========================================')
km = float(input('TOTAL KM:: '))
l = float(input('TOTAL GASOLINE (l):  '))
c = km/l
print(' -------------------------------------------')
print('| CONSUMPTION |   (KM/l)   |    MESSENGER    |')
print('  ------------------------------------------')
print('| smaller than |     8     | Sell the Car !  |')
print('---------------------------------------------')
print('|  between     |  8 and 14 |    Economic  !   |')
print('--------------------------------------------')
print('| heigher than |     12    |  Super Economic! |')
print('---------------------------------------------')


print(f'{c}  km/l')
if c <= 8:
    print('RESULT: SELL THE CAR !')
elif c >= 8 or c <= 14:
    print('RESULT: ECONOMIC !')
elif c >= 12:
    print('RESULT: SUPER ECONOMIC !')
else:
    exit()
