
numero = int(input('Informe um número inteiro: '))
soma = 0


if numero > 0:
    while numero > 0:
        soma += numero % 10
        numero = numero//10
    print(soma)
else:
    print('Número Inválido')
