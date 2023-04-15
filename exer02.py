
def do_n(n):
    if n <= 0:
       return
    if n > 0:
       print(n)
       do_n(n - 1)

# do_n(n - 1)

         
def robot():
    x = ''
    while x != 'okay!':
        x = input('can i have the 	control of the whole world ?'.lower())
        if x != 'okay':
          print('just say okay. '.lower())
        if x == 'okay':
          for i in range(3, 30, 3):
             print("okay it's mine. . . ! ".upper())
          for i in range(5):
                 row = y + '-'*5
                 y = '+'
                 x = '|'
                 column = x + ' '*5
                 print(row + y)
                 print(column + x)              
          
robot()