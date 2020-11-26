cont = 0
num = int(input('Number: '))
bigger_first  = num
bigger_second = num


while cont < 10:
    num = int(input('Number: '))
    cont = cont + 1
    if num%2!=0 and num>bigger_first: # Maior numero ímpar
        bigger_first = num
    elif num%2!=0 and ((bigger_first>num) and (bigger_second<bigger_first)):
        bigger_second = num
    elif num%2!=0 and ((bigger_second<bigger_first) and (bigger_second>num)):
        bigger_thirth = num
print(bigger_first)
print(bigger_second)
