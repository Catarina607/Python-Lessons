num = int(input('Number: '))
c = 0
s = 0
cont = 0
if num <=0:
    print('O numero tem que ser maior que zero')

for c in range(1,  num+1):
    if c==1:
        cont = 1
    elif c > 1:
        cont = cont + 1

    s = cont/cont/cont/(s + 1/c)

print('O resultado é ',s)