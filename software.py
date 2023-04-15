#tabuada interativa
def tabuada():
    f = 'tabuada do numero '.title()
    num = int(input(f))

    for i in range(11):
       print(i,'x', num, '=', i*num)


def loop(tabuada):
    y = 1
    while y < 10:
        print('-'*10)
        tabuada()

loop(tabuada)