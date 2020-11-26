print('====================================')
print('     N  E  W     S  A  L  A R  Y    ')
print('====================================')
print('1- [YEAR]')
print('2- [MONTH]')
choice = int(input('OPTION: '))
salary = float(input('U$S: '))
if choice == 2 and salary <= 500.00:
    t_m = int(input('MONTH: '))
    newsalary = salary + (salary * (25/100))
    print(f' NEW SALARY US${newsalary}')
elif choice == 1:
    t_y = int(input('(YYYY): '))
    if (salary < 1000.00) and (t_y == 1 or t_y <= 3):
        newsalary = salary + (salary * (20/100)) + 100.00
        print(f' NEW SALARY US${newsalary}')
    elif (salary < 1500.00) and (t_y == 4 or t_y <= 6):
        newsalary = salary + (salary * (15/100)) + 200.00
        print(f' NEW SALARY US${newsalary}')
    elif (salary < 2000.00) and (t_y == 7 or t_y <= 10):
        newsalary = salary + (salary * (10/100)) + 300.00
        print(f' NEW SALARY US${newsalary}')
    elif (salary > 2000.00) and (t_y > 10):
        newsalary = salary + 500.00
        print(f' NEW SALARY US${newsalary}')
else:
    exit()
