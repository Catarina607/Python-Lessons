'''
Física - Cinemática 
deltaspc = space 
t = x/60" 
v = deltaspc / (x/60")
s = (deltaspc + v)*(x/60")
area = a = a**3 = ((deltaspc**3)+((×/60")**2))
'''
    
def calc0x():
    import math
    s0= float(input('inicio: '))
    t = float(input('tempo final: '))
    v = int(s0/t)
    s = int(s0+v*t)
    print('='*10)
    a = ((s0**2)+(t**2))       
    a = int(a)
    hip = int(math.sqrt(a))
    area = int(s0 * t)
    senalfa = float(t/hip)
    cosalfa = float(s0/hip)
    tgalfa = float(t/s0)
    print('='*10)
    print('posic init em centimetros:', float(s0))
    print('tempo final sec: ', float(t))
    print('velocidade media constante cm/s: ',float(v))
    print('posicao final metros: ', float(s))
    print('hipotenusa metros de diagonal:', float(hip))
    print('seno alfa: ',senalfa)
    print('cosseno alfa: ',cosalfa)
    print('tangente alfa:', tgalfa)
    print('area do movimento centimetros quadrados: ', int(area))
    
    
def funloop(calc0x):
    while True:
        print('='*10)
        calc0x()
        

funloop(calc0x)

