num = int(input('Number: '))

for number in range(0,  num+1):
        if (number%2==1):
            print(number)
print('--------------------')
for number in range(num+1,  0, -1):
        if (number%2==1):
            print(number)