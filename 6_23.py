num = int(input('Digite n: '))
for c in range(1,  num+1):
    if num % c == 0:
        print(f' {c} ', end=' ')

print('divisores')