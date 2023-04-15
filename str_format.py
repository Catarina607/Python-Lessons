'''
age = 28
name = 'Swaroop'

print('{0} was in {1} years old when he wrote this book'.format(name, age))
print('Why is {0} playing with python'.format(name))
'''
from math import *
def linex3():
    ds = ' '
    l = 'x'*10
    x = ds*8 + l*2
    for i in range(2):
        print(x+x)
    for i in range(1):
        print(x*2)
linex3()
def robot():
    import math
    l = 3
    print('var: {0}'.format(l))
    pi = math.pi
    print('var: {0}'.format(pi))
def looprobot(robot):
    robot()

looprobot(robot)
linex3()