
nota1 = float(input('Nota da Prova de Química: '))

nota2 = float(input('Nota da Prova de Matemática: '))

nota3 = float(input('Nota da Prova de Física: '))

nota1 = nota1 * 1
nota2 = nota2 * 1
nota3 = nota3 * 2
mp = nota1 + nota2 + nota3/1+1+2


if mp >= 60:
    print('Aprovado')
else:
    print('Reprovado')
print(f'A  sua média foi {mp}.')
