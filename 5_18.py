
print('===============================================')
print(' B  A  S  I  C    C  A  L  C  U  L  A  T  E  R ')
print('================================================')
print('Should an option:')
print('[2+2] plus \n[3-2] minus \n[10/5] divided by \n[2x2] times')
should = input('Should a signal: ')
num1 = int(input('Write a number: '))
num2 = int(input('Write another number: '))

if should == '+':
     plus = num1 + num2
     print(f'{num1} + {num2} = {plus}')
elif should == '-':
    minus = num1 - num2
    print(f'{num1} - {num2} = {minus}')
elif should == '/':
    div = num1/num2
    print(f'{num1}:{num2} = {div}')
elif should == '*':
    times = num1 * num2
    print(f'{num1}*{num2} = {times}')
else:
    exit()
