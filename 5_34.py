
grade = float(input('GRADE NUMBER: '))
lack = int(input('LACK NUMBERS: '))


if (grade == 9.0 or grade <= 10.0) and (lack < 20):
    print('A')
elif (grade == 9.0 or grade <= 10.0) and (lack > 20):
    print('B')
elif (grade == 7.5 or grade <= 8.9) and (lack < 20):
    print('B')
elif (grade == 7.5 or grade <= 8.9) and (lack > 20):
    print('C')
elif (grade == 5.0 or grade <= 7.4) and (lack < 20):
    print('C')
elif (grade == 5.0 or grade <= 7.4) and (lack > 20):
    print('D')
elif (grade == 4.0 or grade <= 4.9) and (lack < 20):
    print('D')
elif (grade == 4.0 or grade <= 4.9) and (lack > 20):
    print('E')
elif (grade == 0.0 or grade <= 3.9) and (lack < 20):
    print('E')
elif (grade == 0.0 or grade <= 3.9) and (lack > 20):
    print('E')
else:
    exit()
