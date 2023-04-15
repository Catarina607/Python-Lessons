s = int(input(': '))
n = int(input(': '))
def print_n(s, n):
    if n <= 0:
       return
    print(s)
    print_n(s, n -1)

print_n(s, n)