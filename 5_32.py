
print('==========================================')
print('                M  E  N  U                ')
print('------------------------------------------')
print('| Specifications  |  Code   |   Price    |')
print('|----------------------------------------|')
print("|    Hot-Dog      |   100   |    1.20    |")
print('|----------------------------------------|')
print('|  Simple Bauru   |   101   |    1.30    |')
print("|----------------------------------------|")
print('| Bauru with Eggs |   102   |    1.50    |')
print('|----------------------------------------|')
print('|    Hamburguer   |   103   |    1.20    |')
print('|----------------------------------------|')
print('|  Cheeseburguer  |   104   |    1.70    |')
print('|----------------------------------------|')
print('|     Juice       |   105   |    2.20    |')
print('|----------------------------------------|')
print('|     Soda        |   106   |     1.00   |')
print('|----------------------------------------|')
print('=========================================')
choice = int(input('CODE: '))
product1 = 100
product2 = 101
product3 = 102
product4 = 103
product5 = 104
product6 = 105
product7 = 106
price_1 = 1.20
price_2 = 1.30
price_3 = 1.50
price_4 = 1.20
price_5 = 1.70
price_6 = 2.20
price_7 = 1.00


if choice == 100:
    q = int(input('How many? : '))
    print('Product: Cachorro Quente')
    print(f'Amount: {q}')
    v = price_1*q
    print(f'US$ {v}')
elif choice == 101:
    q = int(input('How many? : '))
    print('Product: Bauru Simples')
    print(f'Amount: {q}')
    v = price_2 * q
    print(f'US$ {v}')
elif choice == 102:
    q = int(input('How many? : '))
    print('Product: Bauru com Ovo')
    print(f'Amount: {q}')
    v = price_3 * q
    print(f'US$ {v}')
elif choice == 103:
    q = int(input('How many? : '))
    print('Product: Hamburguer')
    print(f'Amount: {q}')
    v = price_4 * q
    print(f'US$ {v}')
elif choice == 104:
    q = int(input('How many? : '))
    print('Product: Cheeseburguer')
    print(f'Amount: {q}')
    v = price_5*q
    print(f'US$ {v}')
elif choice == 105:
    q = int(input('How many? : '))
    print('Product: Suco')
    print(f'Amount: {q}')
    v = price_6 * q
    print(f'US$ {v}')
elif choice == 106:
    q = int(input('How many? : '))
    print('Product: Refrigerante')
    print(f'Amount: {q}')
    v = price_7 * q
    print(f'US$ {v}')
else:
    exit()
