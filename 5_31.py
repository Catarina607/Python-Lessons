print('====================================')
print('    WEIGHT AND HEIGHT CALCULATER    ')
print('====================================')
w = float(input('WEIGHT: '))
h = float(input('HEIGHT: '))


if (h <= 1.20) and (w <= 60):
    print('A')
elif(h < 1.20) and (w == 60 or w <= 90):
    print('D')
elif (h < 1.20) and (w >= 90):
    print('G')
elif (h == 1.20 or h <= 1.70) and (w <= 60):
    print('B')
elif (h == 1.20 or h <= 1.70) and (w == 60 or w <= 90):
    print('E')
elif (h == 1.20 or h <= 1.70) and (w >= 90):
    print('H')
elif (h >= 1.70) and (w <= 60):
    print('C')
elif (h >= 1.70) and (w == 60 or w <= 90):
    print('F')
elif (h >= 1.70) and (w >= 90):
    print('I')
else:
    exit()
