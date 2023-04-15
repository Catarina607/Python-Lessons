def grid():
    def row():
    x = int(input('much lines? '.title()))
    a = '+'
    b = '-'
    row = b * x + a
    for i in range(1):
       print(a + row * x)
    def column():
      y = int(input('who much higher ? '.title()))
      a = '|'
      b = ' '
      column = a + b * x
      for i in range(y):
         print(a + column + a)
         

def loopinggrid():
    i = 1
    while i < 10:
        grid()
        
loopinggrid()
