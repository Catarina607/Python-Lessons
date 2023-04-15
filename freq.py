# Frequency 
def vfunc():
    w = float(input('how much waves? '))
        # lambda value
    v = float(input('waves per sec (m/s) '))
    print('*'*10)
        # velocity of the wave
    f = float(((w/v)*10)**2)
        # Frequency in Hertz
    print(f, 'Hertz')
    
# objetive is to put this cond. below linking
# with the function 
'''def fcond(vfunc):
    s_human = int(20000<=20)
        # human perception of sound
    if (f == s_human):
       print('earable by humans')
    if (f > s_human):
       print('Beyond human percption...')
    if (f < float(20)):
       print('Below human earing')

'''

def cont_loop(vfunc):
    while True:
        print('-'*5)
        vfunc()


cont_loop(vfunc)