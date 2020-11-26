
print('==================================')
print('   S M A R T  C A L C U L A T E R ')
print('==================================')
print('Choice an option:')
print('1- Sum of 2 numbers ')
print('2- Diferrence between 2 numbers (higher by lower)')
print('3- The Product between 2 numbers')
print('4- division between 2 numbers (denominator cannot be zero)')

option = int(input('OPTION: '))
num_01 = int(input('NUMBER: '))
num_02 = int(input('NUMBER: '))


if option == 1:
    print('Your Option is to Sum two numbers.')
    s = num_01 + num_02
    print(f' The sum between {num_01}+{num_02}={s}')
elif option == 2:
    print('Your Option is to see Difference between two number.')
    d = num_01 - num_02
    print(f'The Difference between {num_01}-{num_02}={d}')
elif option == 3:
    print('Your option is to see the product betwwen two number.')
    p = num_01*num_02
    print(f'The product between {num_01}x{num_02}={p}')
elif option == 4:
    print('Your Option is a Division between two numbers.')
    div = num_01/num_02
    print(f'The division between {num_01}:{num_02}={div}')
else:
    print('#erro')
