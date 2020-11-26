
print('=================================')
print('        A V E R A G E S          ')
print('     C A L C U L A T E R         ')
print('==================================')
print('[A] GEOMETRIC')
print('[B] WEIGHTED')
print('[C] HARMONICA')
print('[D] ARITHMETIC')
choice = input('Which one average do you want? \n write a letter.:')


if choice == 'A' or choice.lower() == 'a':
    print('[A] GEOMETRIC AVERAGE')
    x = int(input('x: '))
    y = int(input('y: '))
    z = int(input('z: '))
    rootC = (x*y*z)**(1/3)
    print('DEMONSTRATION: ')
    print(f' ³√{x}*{y}*{z} = {rootC}')
elif choice == 'B' or choice.lower() == 'b':
    print('[B] WEIGHTED AVAREGE')
    x = int(input('x: '))
    y = int(input('y: '))
    z = int(input('z: '))
    p1 = int((input(f'weight one: ')))
    p2 = int((input(f'weight two: ')))
    s = p1 + p2
    p = (x+2*y+3*z)/s
    print('DEMONSTRATION: ')
    print(f'  {x}+{p1}*{y}+{p2}*{z}')
    print(f' --------------------  =  {p} ')
    print(f'           {s}           ')
    print(f'THE WEIGHTED AVAREGE IS {p}')
elif choice == 'C' or choice.lower() == 'c':
    print('[C] HARMONICA AVAGERE')
    x = int(input('x: '))
    y = int(input('y: '))
    z = int(input('z: '))
    h = 1/((1/x)+(1/y)+(1/z))
    print('DEMONSTRATION: ')
    print(f'      1     ')
    print(f'  ----------  = {h}')
    print('    1 + 1 + 1')
    print('    -   -   - ')
    print(f'   {x} {y} {z} ')
elif choice == 'D' or choice.lower() == 'd':
    print('[D] ARITHMETIC AVAREGE')
    print('DEMONSTRATION: ')
    x = int(input('x: '))
    y = int(input('y: '))
    z = int(input('z: '))
    a = (x + y + z)/3
    print(f'   {x} + {y} + {z}')
    print(f'   --------------- = {a} ')
    print('             3')
else:
    exit()
