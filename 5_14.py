
print('---------------------------------')
print('     EXAME   DE   LABORATÓRIO    ')
print('---------------------------------')

nota1 = int(input('Nota do Trabalho de Laboratório: '))
nota2 = int(input('Nota da Avaliação Semestral: '))
nota3 = int(input('Nota do Exame Final: '))

nota1= nota1 * 0.0002
nota2= nota2 * 0.0003
nota3 = nota3 * 0.0005
mp = nota1 + nota2 + nota3/0.0002 + 0.0003 + 0.0005
print('============================================')
print(f'        NOTA FINAL: {mp}      ')
print('============================================')


if mp >= 0.0005:
    print('Parabéns! Você esta Aprovado(a)!')
elif mp <= 0.0003 or 0.0049:
    print('Você esta em recuperação.')
elif mp <= 0.0000 or 0.0029:
    print('Ops! Você precisa melhorar.')
    print('Reprovado!')
else:
    exit()
