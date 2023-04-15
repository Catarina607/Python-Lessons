
r = ('+','-','+')
c = ('|',' ','+')
def grid(r, c):
    for i in range(1):
        print(r*4)
    for i in range(4):
        print(c*4)
    for i in range(1):
        print(r*4)

grid(r, c)