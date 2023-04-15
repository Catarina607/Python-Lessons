def lit():
    print('-'*8)
    x = int(input('area: '))
    l = int((1000*x)**3)
    print('if one meter cube is 1 000 l')
    print('it will be', int(l),'liters of water')
    print('into the recipiente')
    print('+','-'*x,'+')
    for i in range(1):
        for i in range(x):
            print('|',' '*int(x),'|')
        print('+','-'*int(x),'+')
 
 
def cool(lit):
    while True:
        lit()
        
        
  
  
cool(lit)

        
