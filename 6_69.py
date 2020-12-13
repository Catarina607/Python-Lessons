a = 0
while a < 10:
    num = int(input('Number: '))
    if num <= 1:
        break
    if num%2>=1:
        print('NUMERO PRIMO')
    if num%2==0:
        print('NUMERO PAR')
    a+=1