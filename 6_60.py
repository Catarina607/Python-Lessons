a = 1000
menor = maior = media = cont = soma = 0
while a > 0:
    num = int(input('Number: '))
    soma += num
    if a == 1:
        cont = 1
    elif a > 1:
        cont = cont + 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if (num < menor) and (num>0):
            menor = num
    if num == 0:
        break
    media = soma/cont
print(' a soma dos numeros é {} e o numero total de digitos é {}'.format(soma,  cont))
print('A média = {}'.format(round(media, 2)))
print('O maior número digitado {} e o menor foi o {}'.format(maior,   menor))

