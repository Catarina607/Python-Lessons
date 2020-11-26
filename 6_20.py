
cont = 0
par = 0
sqc = int(input('qtd: '))

for i in range (1,  sqc+1):
    num = int(input('N: '))
    if num < 1000:
        if (i == 1) and (num%2==0):
            par = num
            cont = 1
            print('par')
        if (i > 1) and (num%2==0):
            par = num
            cont = cont + 1
            print('par')
    else:
        exit()
print('valores pares', cont)