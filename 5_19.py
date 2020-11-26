
num = int(input('Write a number: '))
num_y = num % 3
num_x = num % 5
plus = num_y + num_x


if plus == 0:
    print(f'Oh! no {num} it is simultaneously divisible by 5 and 3')
elif plus > 0 and num_y == 0:
    print(f'Okay! {num} is divisible by 3 and not for 5.')
elif plus > 0 and num_x == 0:
    print(f'Okay! {num} is divisible by 5 and not for 3.')
else:
    print(f'It isnt divisible nor 5 either 3')
