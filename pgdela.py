#Celsius to Fahrenheit 

def convfah():
    x = float(input('Degree in Celsius: '))
    f = float(x * (9.0/5.0))
    print('{0} Fahrenheit'.format(f))
def loopf(conv):
    while True:
        convfah()


loopf(convfah)