par1 = 0
par2 = 0
cont = 0
num = 0
i1 = 0
i2 = 0
contm = 0

for i in range(0,  2):
    num = int(input('N: '))
    if (i == 0) and (num%2==0):
        par1 = num
        cont = 1
    elif (i == 1) and (num%2==0):
        par2 = num
        cont = cont + 1
    if (i == 0) and (num%2!=0):
        i1 = num
        contm = 1
    if (i == 1) and (num%2!=0):
        i2 = num
        contm = contm + 1

soma = par1 + par2 + cont
print(f'impar {i1}*{i2}*{contm} = ', (i1*i2*contm))
print(f'SOMA PARES + DIGITOS: {soma}')