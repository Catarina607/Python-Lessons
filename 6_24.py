num = int(input(' N: '))
soma = 0
for c in range(1, num+1):
    if c == num:
        break
    if num%c==0:
        soma = soma + c
        print(f' + {c} ', end='')
print(f'| soma = {soma}')
