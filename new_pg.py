
vh = float(input('Insert the value of your hour: '))
vhm = float(input('How many hours did work last mouth ?: '))

salary = (vh * vhm)
n_salary = (10*salary)/100
n_new_s = salary + n_salary

print('Your will receive R$ %.2f' % n_new_s)
