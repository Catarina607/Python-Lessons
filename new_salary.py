
print('----------------------------------')
print('        N E W    S A L A R Y      ')
print('----------------------------------')

salary = float(input('write the actual salary of the stuff: '))

n_salary = (26*salary)/100
new_salary = salary + n_salary

print(new_salary,  'is the actual salary')
print('the old salary is ',  salary)
print(f'the new salary with + 26% is {new_salary}')
print(f'so the equation is like {salary} + 26% = {new_salary}')
