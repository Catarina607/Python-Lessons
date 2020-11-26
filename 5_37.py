
print('==================================================')
print('        PARQUIMETRO')
print('==================================================')
print('           ENTRY')
print('--------------------------------------------------')
arrival_hour = int(input('ARRIVAL HOUR: '))
arrival_minutes = int(input('ARRIVAL MINUTE: '))
print('--------------------------------------------------')
print('          EXIT')
print('--------------------------------------------------')
exit_hour = int(input('EXIT HOUR: '))
exit_minutes = int(input('EXIT MINUTE: '))
print('==================================================')
print(f'ARRIVAL = {arrival_hour}:{arrival_minutes}')
print(f'EXIT = {exit_hour}:{exit_minutes}')
totalhour = exit_hour - arrival_hour
totalminutes = exit_minutes - arrival_minutes
print('==================================================')

if (totalhour == 0) and (totalminutes > 0):
    print(f'TOTAL HOURS {abs(totalhour)}:{abs(totalminutes)}')
    hour = 1.00
    print(f'YOU WILL PAY FOR ONE HOUR SERVICE US$ {hour}')
    """ caso o cliente so usou minutos"""
elif (totalhour == 1) and (totalminutes == 0):
    print(f'TOTAL HOURS {abs(totalhour)}:{abs(totalminutes)}')
    hour = 1.00
    print(f'YOU WILL PAY FOR ONE HOUR SERVICE U$S {hour}')
    """caso o cliente tenha usado uma hora exata"""
elif (totalhour == 1) and (totalminutes>1):
    print(f'TOTAL HOURS {abs(totalhour)}:{abs(totalminutes)}')
    hour = 1.00
    print(f'YOU WILL PAY FOR TWO HOURS SERVICE US$ {hour+1.00}')
    """caso o cliente usou 1 e alguns minutos"""
elif (totalhour == 2) and (totalminutes == 0):
    print(f'TOTAL HOURS {abs(totalhour)}:{abs(totalminutes)}')
    hour = 1.00
    print(f'YOU WILL PAY FOR TWO HOUR SERVICE U$S {hour+1.00}')
    """caso o cliente tenha usado duas horas exata"""
elif (totalhour == 2) and (totalminutes>=1):
    print(f'TOTAL HOURS {abs(totalhour)}:{abs(totalminutes)}')
    hour = 1.40
    print(f'YOU WILL PAY FOR THREE HOURS SERVICE US$ {hour*3}')
    """caso o cliente usou duas horas e alguns minutos mais vai ser cobrada como 3horas"""
elif (totalhour == 3) and (totalminutes == 0):
    print(f'TOTAL HOURS {abs(totalhour)}:{abs(totalminutes)}')
    hour = 1.40
    print(f'YOU WILL PAY FOR THREE HOUR SERVICE U$S {hour*3}')
    """caso o cliente tenha usado três horas exata"""
elif (totalhour == 3) and (totalminutes>=1):
    print(f'TOTAL HOURS {abs(totalhour)}:{abs(totalminutes)}')
    hour = 1.40
    print(f'YOU WILL PAY FOR FOUR HOURS SERVICE US$ {hour*4}')
    """caso o cliente usou três horas e alguns minutos vai ser cobrada como se tivesse usado 4 horas"""
elif (totalhour == 4) and (totalminutes == 0):
    print(f'TOTAL HOURS {abs(totalhour)}:{abs(totalminutes)}')
    hour = 1.40
    print(f'YOU WILL PAY FOR FOUR HOURS SERVICE U$S {hour*4}')
    """caso o cliente tenha usado 4 horas exata"""
elif (totalhour == 4) and (totalminutes>=1):
    print(f'TOTAL HOURS {abs(totalhour)}:{abs(totalminutes)}')
    hour = 2.00
    print(f'YOU WILL PAY FOR FIVE HOURS SERVICE US$ {hour*5}')
    """caso o cliente usou 4 horas e alguns minutos vai ser cobrada como se tivesse usado 5 horas"""
elif (totalhour == 5) and (totalminutes == 0):
    print(f'TOTAL HOURS {abs(totalhour)}:{abs(totalminutes)}')
    hour = 2.00
    print(f'YOU WILL PAY FOR FIVE HOURS SERVICE U$S {hour*5}')
    """caso o cliente tenha usado 5 horas exata"""
elif (totalhour == 5) and (totalminutes>=1):
    print(f'TOTAL HOURS {abs(totalhour)}:{abs(totalminutes)}')
    hour = 2.00
    print(f'YOU WILL PAY FOR FIVE HOURS SERVICE US$ {hour*6}')
    """caso o cliente usou 5 horas e alguns minutos vai ser cobrada como se tivesse usado 6 horas"""
elif (totalhour >= 5) and (totalminutes == 0):
    print(f'TOTAL HOURS {abs(totalhour)}:{abs(totalminutes)}')
    hour = 2.00
    print(f'YOU WILL PAY FOR ONE HOUR SERVICE U$S {hour*totalhour}') #hora preço vezes hora liquida
    """caso o cliente tenha usado mais de 5 horas horas exata"""
elif ((totalhour >= 5) and (totalhour <= 12)) and (totalminutes>=1):
    hour = 2.00
    print(f'YOU WILL PAY FOR TWO HOURS SERVICE US$ {(hour*totalhour)+hour}') # hora exata + hora minuto
    """caso o cliente usou mais de 5 horas e alguns minutos vai ser cobrada como se tivesse usado 6 horas"""
if arrival_hour>exit_hour:
    print('YOU EXPENDEND MORE THAN ONE DAY HERE')
    exit_hour = (24 - (24 - exit_hour))
    print(f'{int(exit_hour)}:{totalminutes} ****')
    if (int(exit_hour) == 1) and (totalminutes == 0):
        if totalminutes < 0:
            totalminutes = totalminutes + totalminutes
        hour = 1.00
        print(f'TOTAL HOURS {abs(exit_hour)}:{abs(totalminutes)}')
        print(f'YOU WILL PAY FOR ONE HOUR SERVICE U$S {hour}')
    elif (int(exit_hour) == 1) and (totalminutes > 1):
        if totalminutes < 0:
            totalminutes = totalminutes + totalminutes
        print(f'TOTAL HOURS {abs(exit_hour)}:{abs(totalminutes)}')
        hour = 1.00
        print(f'YOU WILL PAY FOR TWO HOURS SERVICE US$ {hour + 1.00}')
    elif (int(exit_hour) == 2) and (totalminutes == 0):
        if totalminutes < 0:
            totalminutes = totalminutes + totalminutes
        print(f'TOTAL HOURS {abs(exit_hour)}:{abs(totalminutes)}')
        hour = 1.00
        print(f'YOU WILL PAY FOR TWO HOUR SERVICE U$S {hour + 1.00}')
    elif (int(exit_hour) == 2) and (totalminutes >= 1):
        if totalminutes < 0:
            totalminutes = totalminutes + totalminutes
        print(f'TOTAL HOURS {abs(exit_hour)}:{abs(totalminutes)}')
        hour = 1.40
        print(f'YOU WILL PAY FOR THREE HOURS SERVICE US$ {hour * 3}')
    elif (int(exit_hour) == 3) and (totalminutes == 0):
        if totalminutes < 0:
            totalminutes = totalminutes + totalminutes
        print(f'TOTAL HOURS {abs(exit_hour)}:{abs(totalminutes)}')
        hour = 1.40
        print(f'YOU WILL PAY FOR THREE HOUR SERVICE U$S {hour * 3}')
    elif (int(exit_hour) == 3) and (totalminutes >= 1):
        if totalminutes < 0:
            totalminutes = totalminutes + totalminutes
        print(f'TOTAL HOURS {abs(exit_hour)}:{abs(totalminutes)}')
        hour = 1.40
        print(f'YOU WILL PAY FOR FOUR HOURS SERVICE US$ {hour * 4}')
    elif (int(exit_hour) == 4) and (totalminutes == 0):
        if totalminutes < 0:
            totalminutes = totalminutes + totalminutes
        print(f'TOTAL HOURS {abs(exit_hour)}:{abs(totalminutes)}')
        hour = 1.40
        print(f'YOU WILL PAY FOR FOUR HOURS SERVICE U$S {hour * 4}')
    elif (int(exit_hour) == 4) and (totalminutes >= 1):
        if totalminutes < 0:
            totalminutes = totalminutes + totalminutes
        print(f'TOTAL HOURS {abs(exit_hour)}:{abs(totalminutes)}')
        hour = 2.00
        print(f'YOU WILL PAY FOR FOUR HOURS SERVICE U$S {hour * 4}')
    elif (int(exit_hour) == 5) and (totalminutes == 0):
        if totalminutes < 0:
            totalminutes = totalminutes + totalminutes
        print(f'TOTAL HOURS {abs(exit_hour)}:{abs(totalminutes)}')
        hour = 2.00
        print(f'YOU WILL PAY FOR FIVE HOURS SERVICE U$S {hour * 5}')
    elif (int(exit_hour) == 5) and (totalminutes >= 1):
        if totalminutes < 0:
            totalminutes = totalminutes + totalminutes
        print(f'TOTAL HOURS {abs(exit_hour)}:{abs(totalminutes)}')
        hour = 2.00
        print(f'YOU WILL PAY FOR FIVE HOURS SERVICE US$ {hour * 6}')
    elif (int(exit_hour) >= 5) and (totalminutes == 0):
        if totalminutes < 0:
            totalminutes = totalminutes + totalminutes
        print(f'TOTAL HOURS {abs(exit_hour)}:{abs(totalminutes)}')
        hour = 2.00
        print(f'YOU WILL PAY FOR {exit_hour} HOURS SERVICE U$S {hour * exit_hour}')
    elif (int(exit_hour) >= 5) and (totalminutes >= 1):
        if totalminutes < 0:
            totalminutes = totalminutes + totalminutes
        hour = 2.00
        print(f'TOTAL HOURS {abs(exit_hour)}:{abs(totalminutes)}')
        print(f'YOU WILL PAY FOR TWO HOURS SERVICE US$ {(hour * exit_hour) + hour}')
