
def convctofah():
    c = float(input('Celsius (°) '))
    f = c * (9.0/5.0)+32.0
    print('{0} ° Fahrenheit'.format(f))
    choosop(choose)
'''
 Converter to Fahrenheit.
'''
def looptofah():
    while True:
          convctofah()
          
def fahtocels():
    f = float(input('Fahrenheit (°)'))
    c = 5.0 * (f - 32.0)/9.0
    print('{0} ° Celsius'.format(c))
    choosop(choose)

def looptocels():
    while True:
        fahtocels()
        
def kelvintocels():
    k = float(input('in Kelvin '))
    c = k - 273.15
    print('{0} ° Celsius'.format(c))
    choosop(choose)
    
def loopktoc():
    while True:
        kelvintocels()
        
def celstokelv():
    c = float(input('in Celsius '))
    k = c + 273.15
    print('{0} Kelvin'.format(k)) 
    choosop(choose)
    
def looptok():
    while True:
        celstokelv()
                  
def choose():
    o = '-'*10
    print('[1] Celsius to Fahrenheit ')
    print('[2] Fahrenheit to Celsius ')
    print('[3] Kelvin to Celsius ')
    print('[4] Celsius to Kelvin')
    print(o)
    x = int(input())
    print(o)
    if x == 1:
       looptofah()
      
    if x == 2:
       looptocels()
       
    if x == 3:
       loopktoc()
       
    if x == 4:
       looptok()
    if x >= 5:
       choose()
    if x <= 0:
       choose()

def choosop(choose):
    l = 'quer continuar...?'
    y = '-'*10
    print(y)
    print(l)
    m = str(input('S ou N ?'))
    print('-'*5)
    print(m)
    if (m == 's'.upper()) or (m == 's'.lower()) :
        choose()
    else:
        exit()   

def wantagain(choose):
    while True:
         print('-'*10)
         s = ' '
         w = 'Converso de Temperaturas'.lower()
         print(s*4 + w)
         print('-'*10)     
         choose()      
    
    
def louping():
    while True:
        wantagain(choose)
while True:
    louping()
    
