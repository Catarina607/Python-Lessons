
print('==================================')
print('               IMC                ')
print('==================================')
w = float(input('WEIGHT: '))
h = float(input('HEIGHT: '))
imc = w/(h**2)


if imc < 18.5:
    print('UNDER WEIGHT')
elif imc == 18.6 or imc <= 24.9:
    print('HEALTHY')
elif imc == 25.0 or imc <= 29.9:
    print('EXCESS WEIGHT')
elif imc == 30.0 or imc <= 34.9:
    print('GRADE I OBESITY')
elif imc == 35.0 or imc <= 39.9:
    print('GRADE II OBESITY')
elif imc >= 40.0:
    print('GRADE III OBESITY')
else:
    exit()
