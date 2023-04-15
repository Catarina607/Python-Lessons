def callrobot():
    while True:
        comando = input("Digite 'sair' para sair: ".title())
        if comando == 'sair':
            break
    
    for num in range(1, 11):
        if num == 6:
           break
        else:
           print(num)
    print('Sai do loop')  

callrobot()


