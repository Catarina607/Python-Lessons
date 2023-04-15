'''

onda de sonora (radio)
parametro do out vai me dar o valor do input,
por extenso em hertz(hz)

'''
def megahz():
    import math
    exp = 10**6
    x = float(input('hertz: '))
    f = float(x*exp)
    print('megahz frequency')
    print(float(f),'hertz')
    print('-'*10)

def loophertz(megahz):
    while True:
        megahz()
        
loophertz(megahz)