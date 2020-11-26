
print('=================================')
print('      S W I M M E R  C L A S S   ')
print('=================================')
age = int(input('Age: '))


if age == 5 or age <= 7:
    print(f'AGE: {age}')
    print('CATEGORY: childish A')
elif age == 8 or age <= 10:
    print(f'AGE: {age}')
    print('CATEGORY: childish B')
elif age == 11 or age <= 13:
    print(f'AGE: {age}')
    print('CATEGORY: Juvenile A')
elif age == 14 or age <= 17:
    print(f'AGE: {age}')
    print('CATEGORY: Juvenile B')
elif age > 18:
    print(f'AGE: {age}')
    print('CATEGORY: Senior')
else:
    exit()
