#Teorema de Pitágoras 
ob = float(input('hight ponto OB semi-reta: '))
oc = float(input('length ponto OC semi-reta:'))

def cool(ob, oc):
    import math
    a = (ob ** 2) + (oc **2)
    a = float(a ** 2)
    print(a**2,'m2')
    sqrt = math.sqrt(a)
    print('hipotenusa', sqrt)
    print('×'*10)
    print('Bidimensional')
    print('x'*10)
    
def grid():
     # row for i in range
    
    
    for i in range(1):
        print('-'*ob)
    for i in range(1):
        print('-'*oc)
    # column for i in range    
    
    
    
def loopfunc(cool, grid):
    while True:
        cool()
        grid()
        
        
        
loopfunc(cool, grid)