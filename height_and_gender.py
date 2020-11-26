
h = float(input('Height: '))
bsex = str(input('Biologic Sex [F/M]: '))
if bsex == 'f' or bsex == 'F':
    w = (72.7 * h) - 58
    print('IDEAL WEIGHT %.2f'%w)
elif bsex == 'm' or bsex == 'M':
    w = (62.1*h) - 44.7
    print('IDEAL WEIGHT %.2f'%w)
else:
    exit()
