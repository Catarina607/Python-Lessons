

num1 = int(input('Number: '))
num2 = int(input('Number: '))
num3 = int(input('Number: '))


if num1 > num2 and num1 > num3:
    print(num1)
    if num2 > num3:
        print(num2)
        print(num3)
    else:
        print(num3)
        print(num2)
elif num2 > num1 and num2 > num3:
    print(num2)
    if num3 > num1:
        print(num3)
        print(num1)
    else:
       print(num1)
       print(num3)
elif num3 > num2 and num3 > num1:
    print(num3)
    if num2 > num1:
        print(num2)
        print(num1)
    else:
        print(num1)
        print(num2)
else:
    print('Thank you !')
