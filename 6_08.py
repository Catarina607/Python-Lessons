numb = 0
num = int(input('Number: '))
maior = num
menor = num

while numb < 9:
    num = int(input('Number: '))
    numb = numb + 1

    if num > maior:
        maior = num
    if num < menor:
        menor = num
print(maior)
print(menor)
