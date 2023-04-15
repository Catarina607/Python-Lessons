''' 

row x4
'''


def row():
    sy = ' '
    x = '+'
    linex = '-'*4
    row = x + linex
    for i in range(1):
        print(sy*10+(row*4)+x)
'''

column x4
'''            
def column():
    sx = ' '
    y = '|'
    vy= y + sx*4 
    for i in range(1):
        print(sx*10+vy*4+y)


def grid(row, column):
    row()
    column()
    
def templant():
    nonespace = ' '*10
    for i in range(2):
        print(nonespace)
        
liney = '-'
def parameter(liney):
    for i in range(1):
        print(liney*40)     
'''
Bidimensional  area in m2

'''   

templant()
parameter(liney)
print('length x = 4')
parameter(liney)
templant()
grid(row, column)
grid(row, column)
row()
templant()
parameter(liney)
print('hight y = 2')
parameter(liney)

def areafun():
    import math
    b = 4
    c = 2
    a = b*c
    print('4×2 =',a,'m2')
    sen = float(c/a)
    print(sen,'sen alfa')
areafun()
