#robot assistente da Jessica
def another_robot():
    number = range(10)
    for i in range(10):
        print(number)
        
def her_robot(another_robot):
    name = input('qual e o seu nome? '.title())
    print(name)
    answer = ''
    yes = 'sim'.lower() or 'sim'.upper() or 'sim'.title() or 's'.upper() or 's'.lower()
    no = 'nao'.upper() or 'nao'.lower() or 'nao'.title() or 'n'.upper() or 'n'.lower() or 'no'.upper() or 'no'.lower() or 'no'.title()
    while answer != yes:
          answer = input('Já acabou, ' + name +'?')
          
    while answer == no:
          another_robot()

her_robot()
