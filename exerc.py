# think python
l = int(input(':'))
def grid(l):
    for i in range(1):
        print('+','-'*l,'+','-'*l,'+')
        for i in range(l):
            print('|',' '*l,'|',' '*l,'|')
    for i in range(1):
        print('+','-'*l,'+','-'*l,'+')
def ggrid(l):
    for i in range(l):
        print('|',' '*l,'|',' '*l,'|')
    for i in range(1):
        print('+','-'*l,'+','-'*l,'+')
      
      
def cloop(grid=l, ggrid=l):
        grid(l)
        ggrid(l)

cloop(grid, ggrid)