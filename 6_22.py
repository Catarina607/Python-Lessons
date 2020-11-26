grade = 0
sm = 0
m = 0
ng = int(input(' amount: '))
media = 0

for i in enumerate(range(0,  ng)):
    grade = float(input(f' grade: '))
    if (grade >=10.0) and (grade <= 20.0):
        sm = sm + grade
        m = sm/ng
    else:
        exit()
print('media = % 2.f'% m)
