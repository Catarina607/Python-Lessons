    def block():
    import math
    print('×'*10)
    x = float(input('length m: '))
    y = float(input('hight m: '))
    print('×'*10)
    print('Area:',int(x),'lengths x',int(y),'hights')
    print('Area: ',int(x*y),'square meters.')
    dig = int((x*y)/2)
    print('Diagonal (hipotenusa em metros)',dig)
    print('×'*10)
    a = float(14.34)
    p = float(a*(x*y))
    print(' it will be $', float(p))
    print(' there is no taxes added.')
    print('~'*25)
    print('+','-'*int(x),'+')
    for i in range(int(y)):
        print('|',' '*int(x),'|')
    print('+','-'*int(x),'+') 
    print('~'*25)
    print('$'*(4*10))
def uy(block):
    while True:
          block()
          
while True:
    print('$'*(4*10))
    uy(block)
            
   
    
