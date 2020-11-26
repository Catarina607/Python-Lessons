
print('====================================')
print('             PRODUCT TAX            ')
print('====================================')

value = int(input('Value US$: '))
print(' How much percents ?')
print('[5%] for values lesss than U$S50')
print('[10%] for values between US$50 and U$S100')
print('[15%] for values heighter than U$S100')
amount = int(input('Amount: '))
p = amount/100
new = value + (value * p)
print('PRICE: US$',  new)

if new < 80:
    print('Result: Cheap')
elif new == 80 or new < 120:
    print('Result: Normal')
elif new == 120 or new < 200:
    print('Result: Expensive')
elif new > 200:
    print('Result: Much Expensive')
else:
    exit()

