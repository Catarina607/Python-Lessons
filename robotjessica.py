# Frequency 
def vfunc():
    while True:
        w = float(input('how much waves? '))
        # lambda value
        v = float(input('waves per sec (m/s) '))
        print('*'*10)
        # velocity of the wave
        f = float(((w/v)*10)**2)
        # Frequency in Hertz
        print(f, 'Hertz')
'''
def cont_loop(vfunc):
    while True:
        print('-'*5)
        vfunc()
'''
def robot(vfunc):
    r = ''
    while r != 'sim':
          r = input('Ja acabou, Catarina Chiara ?'.title())
    vfunc()      


# robotdela(vfunc)
def loopin():
    num = 10
    while num > 1:
        robot(vfunc)
        return

loopin()        
        
   