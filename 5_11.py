
import math

num = int(input('Write a number: '))


if num > 0:
    log_num = math.log(num)
    print('the log of this number is %.2f'%log_num)
else:
    print('INVALID NUMBER')
