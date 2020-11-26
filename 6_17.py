
print('OBS: \n measure should be in meters.')
print('================================')
bigger_base = float(input('Write the biggest base of the trapeze: '))
print('the Biggest base should be different of 0')
lower_base = float(input('Write the lowest base of the trapeze: '))
height = float(input('Write the height of the Trapeze: '))


if lower_base >= bigger_base:
    print('Invalid Sentence')
else:
    a = (bigger_base + lower_base) * height/2
    print(f'The area of the Trapeze is equal {a} m²')
