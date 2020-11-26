print('INFORMATION: if is 1, 2, 3,... put 01, 02, 03,...')
print(' 24 hours format')
arrival_hour = int(input('ARRIVAL HOUR: '))
arrival_minutes = int(input('ARRIVAL MINUTE: '))
exit_hour = int(input('EXIT HOUR: '))
exit_minutes = int(input('EXIT MINUTE: '))
print('--------------------------------------')
print(f'ARRIVAL = {arrival_hour}:{arrival_minutes}')
print(f'EXIT = {exit_hour}:{exit_minutes}')
totalhour = exit_hour - arrival_hour
totalminutes = exit_minutes - arrival_minutes
print('--------------------------------------')

newvar = (exit_hour + 24) - arrival_hour
var_min =exit_minutes - arrival_minutes
var_min = (var_min - var_min)
print(f'{newvar}:{var_min}')


'''if (newvar == 3) and (var_min == 0):
        hour = 1.00
        print(f'YOU WILL PAY FOR ONE HOUR SERVICE U$S {hour} \n |EXPENDED = {newvar}:{var_min}')
elif (newvar == 3) and (var_min >= 1):
        hour = 1.00
        print(f'YOU WILL PAY FOR ONE HOUR SERVICE U$S {hour} \n |EXPENDED = {newvar}:{var_min}')
elif (newvar == 4) and (var_min == 0):
        hour = 1.00
        print(f'YOU WILL PAY FOR ONE HOUR SERVICE U$S {hour} \n |EXPENDED = {newvar}:{var_min}')
elif (newvar == 4) and (var_min >= 1):
        hour = 1.00
        print(f'YOU WILL PAY FOR ONE HOUR SERVICE U$S {hour} \n |EXPENDED = {newvar}:{var_min}')
'''
'''if (newvar == 1) and (totalminutes == 0):
        hour = 1.00
        print(f'YOU WILL PAY FOR ONE HOUR SERVICE U$S {hour} \n |EXPENDED = {newvar}:{totalminutes}')
elif (newvar == 1) and (totalminutes > 1):
        hour = 1.00
        print(f'YOU WILL PAY FOR ONE HOUR SERVICE U$S {hour} \n |EXPENDED = {newvar}:{totalminutes}')
elif (newvar == 2) and (totalminutes == 0):
        hour = 1.00
        print(f'YOU WILL PAY FOR ONE HOUR SERVICE U$S {hour} \n |EXPENDED = {newvar}:{totalminutes}')
elif (newvar == 2) and (totalminutes >= 1):
        hour = 1.00
        print(f'YOU WILL PAY FOR ONE HOUR SERVICE U$S {hour} \n |EXPENDED = {newvar}:{totalminutes}')
elif (newvar == 3) and (totalminutes == 0):
        hour = 1.00
        print(f'YOU WILL PAY FOR ONE HOUR SERVICE U$S {hour} \n |EXPENDED = {newvar}:{totalminutes}')
elif (newvar == 3) and (totalminutes >= 1):
        hour = 1.00
        print(f'YOU WILL PAY FOR ONE HOUR SERVICE U$S {hour} \n |EXPENDED = {newvar}:{totalminutes}')
elif (newvar == 4) and (totalminutes == 0):
        hour = 1.00
        print(f'YOU WILL PAY FOR ONE HOUR SERVICE U$S {hour} \n |EXPENDED = {newvar}:{totalminutes}')
elif (newvar == 4) and (totalminutes >= 1):
        hour = 1.00
        print(f'YOU WILL PAY FOR ONE HOUR SERVICE U$S {hour} \n |EXPENDED = {newvar}:{totalminutes}')
elif (newvar == 5) and (totalminutes == 0):
        hour = 1.00
        print(f'YOU WILL PAY FOR ONE HOUR SERVICE U$S {hour} \n |EXPENDED = {newvar}:{totalminutes}')
elif (newvar == 5) and (totalminutes >= 1):
        hour = 2.00
        print(f'YOU WILL PAY FOR FIVE HOURS SERVICE US$ {hour * 6}  \n |EXPENDED = {newvar}:{totalminutes}')
elif (newvar >= 5) and (totalminutes == 0):
        hour = 1.00
        print(f'YOU WILL PAY FOR ONE HOUR SERVICE U$S {hour} \n |EXPENDED = {newvar}:{totalminutes}')
elif (newvar >= 5) and (totalminutes == 0):
        hour = 2.00
        print(f'YOU WILL PAY FOR {hour} SERVICE U$S {hour * totalhour}  \n |EXPENDED = {newvar}:{totalminutes}')
elif (newvar >= 5) and (totalminutes >= 1):
        hour = 1.00
        print(f'YOU WILL PAY FOR ONE HOUR SERVICE U$S {hour} \n |EXPENDED = {newvar}:{totalminutes}')
'''