num = int(input('N: '))
soma1 = 0
soma2 = 0
for c in range(1, num+1):
    if num <= 1000:
        if num%5==0:
            if c%5==0:
                print(f' {c} ', end='')
                soma1 = soma1 + c
        if num%3==0:
            if c%3==0:
                 print(f' {c} ', end='')
                 soma2 = soma2 + c

if soma1>=1:
    print(f'| SOMA = {soma1} ')
if soma2>=1:
    print(f'| SOMA = {soma2}')
elif soma2==0 or soma1==0:
    exit()
