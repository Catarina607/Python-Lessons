#Fahrenheit to Celsius
def convc():
    y = float(input('Fahrenheit temper:'))
    c = 5.0 * (y - 32.0)/9.0
    print('Celsius {0} °'.format(c))

def loopc(convc):
    while True:
          convc()

loopc(convc)