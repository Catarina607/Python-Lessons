
print('==============================')
print('            COMISSION         ')
print('==============================')
value = float(input('US$: '))

if value >= 100.000:
    p = value * (16/100)
    c = 700.00 + p
    print(f'COMISSION: US${c}')
elif (value < 100.000) and (value >= 80.000):
     p = value * (14/100)
     c = 650.00 + p
     print(f'COMISSION: US${c}')
elif (value < 80.000) and (value >= 60.000):
    p = value * (14/100)
    c = 600.00 + p
    print(f'COMISSION: US${c}')
elif (value < 60.000) and (value >= 40.000):
    p = value * (14/100)
    c = 550.00 + p
    print(f'COMISSION: US${c}')
elif (value < 40.000) and (value >= 20.000):
    p = value * (14/100)
    c = 500.00 + p
    print(f'COMISSION: US${c}')
elif value < 20.000:
    p = value * (14/100)
    c = 400.00 + p
    print(f'COMISSION: US${c}')
else:
    exit()
