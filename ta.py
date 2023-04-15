x = 'hello'.upper()
n = int(input('|  : '))
def print_n(x, n):
    if n <= 0:
       return
    print(x)
    print_n(x, n -1)

print_n(x, n)