soma = 0
media = 0
maior = 0

for num in range(1, 10):
    value = int(input('Number: '))
    if value < 0:
        zero = value
    elif value > 0:
        soma = soma + value
        media = soma/2
print(f'{media}')