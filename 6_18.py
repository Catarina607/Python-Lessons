i = 0
maior = 0
cont = 0
n = int(input('qtd de n: '))

for i in range(1,  n):
    num = int(input(f'informe o {i}º numero: '))
    if i == 1:
        maior = num
        cont = 1
    elif (maior < num):
        maior = num
        cont = 1
    elif maior == num:
        cont = cont + 1
print(f'{maior} maior,{cont} vezes')