
print('=================================')
print('       RETIREMENT CONDITION      ')
print('=================================')

age = int(input('Age: '))
t_service = int(input('Time of Service: '))

if age == 65 or t_service > 30:
    print('You Can Retire.')
elif age == 65 and t_service >= 25:
    print('You Can Retire.')
else:
    print('You cannot Retire')
