
print('------------------------------------')
print('       T  E  S  T    M E            ')
print('------------------------------------')
salary = float(input('Write your salary US$:  '))
prest = int(input('Price of the installment US$:  '))
emp = prest/salary
perct = emp * 100


if perct > 20.0:
    print('unsecured loan')
else:
    print('loan granted')
