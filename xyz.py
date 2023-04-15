#precisa de correcao de bugs
def kmph_mps():
#speed converter| choice [1]
    v = float(input('km/h (velocity)'))
    m = v / 3.6
'''
   [equation to converte velocity
   to m/s.]
'''
   print(v + ' km/h')
   print('{0} m/s'.format(m))
   
def mpsconv():
# choice [2]
    v = float(input('m/s (velocity) '))
    k = v * 3.6
'''
    [equation to converte velocity
    in m/s to km/h]
'''
    print(v + 'm/s')
    print('{0} km/h'.format(k))
    
def milha_km():
# choice [3]
    m = float(input('milhas distancy: '))
    distkm = 1.61 * m
'''
    [equation to converte 
    milhas distance
    to km segmenter
    point A to point B.]
'''
    print('{0} km'.format(distkm))
    
def km_milhas():
# choice [4]
    k = float(input('km distance: '))
    distmilhas = k/1.61
'''
    [equation to converte km distance 
    to milhas.
    variation space in milhas 
    var m]
'''
    print(float('{0} km'.format(k)))
    print('{0} milhas'.format(distmilhas))
    
    
def row():
    a = '×'*10
    for i in range(1):
        print(a)

def choices(row):
'''
    [Menu]
'''
    row()
    a = ' '
    print(a*4 + 'speed converter'.upper())
    print(a + 'km/h to m/s [1]'.upper())
    print(a + 'm/s to km/h [2]'.upper())
    print(a + 'milhas to km [3]'.upper())
    print(a + 'km to milhas [4]'.upper())
    row()
    op = int(input(a + '[O P T I O N S] '.upper()))
    print(op)
    row()
'''
    [integer who will give the input to given  
    options.]
'''
    if (op >= 0 or op <= 4):
      if op == 1:
        kmph_mps()
      if op == 2:
        mpsconv()
      if op == 3:
        milha_km()
      if op == 4:
        km_milhas()
    else:
        pass
           
choices()


'''
def looprepeat(choose):
    while True:
        choose()

looprepeat(choose)
'''