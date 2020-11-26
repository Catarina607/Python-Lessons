soma = 0
a = int(input('Number: '))
b = str(a)
for i in range(len(b)):
    soma += int(b[i])
print(soma)