import math
shoplist = ['apple','mango','carret','banana']
name = 'swaroop'
def bull(shoplist, name):
    
    # indexing or Subscription operation
    print('Item 0 is', shoplist[0])
    print('Item 1 is', shoplist[1])
    print('Item 2 is', shoplist[2])
    print('Item 3 is', shoplist[3])
    print('Item -1 is', shoplist[-1])
    print('Item -2 is', shoplist[-2])
    print('Character 0 is', name[0])
    # slicing in a list
    print('Item 1 to 3 is', shoplist[1:3])
    print('Item 2 to end is', shoplist[2:])
    print('Item 1 to -1 is', shoplist[1:-1])
    print('start to end is', shoplist[:])
    # slicing on a string #
    print('character 1 to 3 is', name[1:3])
    print('character 2 to end is', name[2:])
    print('character 1 to -1 is', name[1:-1])
    print('character start to end is', name[:])
def lol():
    bull(shoplist, name)
lol()
q = int(input())
for i in range(q):
    flag = True
    if flag: print('Yes')

points = [{'x':2, 'y':3},
          {'x':4, 'y':1}]
points.sort(key=lambda i: i['y'])
print(points)
        
    
    
       
 
       
