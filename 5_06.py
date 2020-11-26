
print('------------------------------------')
print('   P  R  O  G  R  A  M  M  I  N  G  ')
print('------------------------------------')
num1 = int(input('Write a number: '))
num2 = int(input('Write another number: '))


if num1 > num2:
    print(f'{num1} is the bigger one')
    print(f'The difference between {num1} and {num2} is {num1-num2}')
elif num1 == num2:
    print('The numbers are equal')
else:
    print(f'{num2} is the bigger one')
    print(f'The difference between {num2} and {num1} is {num2-num1}')
