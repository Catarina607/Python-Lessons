x = int(input('  [1]: '))
y = int(input('  [2]: '))
n = int(input('  [3]: '))
def p(x, y, n):
    ds = ' '*2
    print(str(ds) + 'countness: {0} | {1} | {2}'.format(x,y,n))
    s =  x + y + n
    s = int(s)
    print('  sum: {0}'.format(s))


def loopf(p):
    for i in range(5):
          p(x,y,n)

loopf(p)