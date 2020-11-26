num = int(input('N: '))

for c in range(1, num+1):
    if num%11==0:
        if c%11==0:
            print(c)
    elif num%13==0:
        if c%13==0:
            print(c)
    elif num%17==0:
        if c%17==0:
            print(c)
