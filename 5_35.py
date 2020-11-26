
print('=====================================')
print('           DAY AND MOUNTH           ')
print('=====================================')
day = int(input('NUMERIC DAY: '))
month = int(input('NUMBER OF THE MONTH: '))

if (month == 1) and ((day <= 31) and (day >= 1)):
    print(f'{day}/{month}/2020')
    print(f'{day} of January')
elif (month == 2) and ((day <= 29) and (day >= 1)):
    print(f'{day}/{month}/2020')
    print(f'{day} of February')
elif (month == 3) and ((day <= 31) and (day >= 1)):
    print(f'{day}/{month}/2020')
    print(f'{day} of March')
elif (month == 4) and ((day <= 30) and (day >= 1)):
    print(f'{day}/{month}/2020')
    print(f'{day} of April')
elif (month == 5) and ((day <= 31) and (day >= 1)):
    print(f'{day}/{month}/2020')
    print(f'{day} of May')
elif (month == 6) and ((day <= 30) and (day >= 1)):
    print(f'{day}/{month}/2020')
    print(f'{day} of June')
elif (month == 7) and ((day <= 31) and (day >= 1)):
    print(f'{day}/{month}/2020')
    print(f'{day} of July')
elif (month == 8) and ((day <= 31) and (day >= 1)):
    print(f'{day}/{month}/2020')
    print(f'{day} of August')
elif (month == 9) and ((day <= 30) and (day >= 1)):
    print(f'{day}/{month}/2020')
    print(f'{day} of September')
elif (month == 10) and ((day <= 31) and (day >= 1)):
    print(f'{day}/{month}/2020')
    print(f'{day} of October')
elif (month == 11) and ((day <= 30) and (day >= 1)):
    print(f'{day}/{month}/2020')
    print(f'{day} of November')
elif (month == 12) and ((day <= 31) and (day >= 1)):
    print(f'{day}/{month}/2020')
    print(f'{day} of December')
else:
    print('DATA: INVALID SINTAX')


if month > 12 or month < 1:
    print('MONTH: WRONG!')
elif month <= 12:
    print('MONTH: VALID SINTAX!')
else:
    exit()

