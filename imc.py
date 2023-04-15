
def imc():
    kg = float(input('peso(kg) : '))
    h = float(input('Altura em m: '))
    imc = kg/h**2
    print('-'*8)
    info = 'IMC {0}'.format(imc)
def kgh(imc):
    if (imc < 18.5):
       print(info)
       print('Abaixo do Peso')
    if (imc == 18.5) or (imc == 24.9):
       print(info)
       print('Peso Normal')
    if (imc == 25) or (imc == 29.9):
       print(info)
       print('Sobrepeso')
    if (imc == 30) or (imc == 34.9):
       print(info)
       print('Obesidade Grau 1')
    if (imc == 35) or (imc == 39.9):
       print(info)
       print('Obesidade Grau 2')
    if imc >= 40:
       print(info)
       print('Obesidade Grau 3')
    else:
       pass

imc()
kgh(imc)