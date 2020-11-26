
value = float(input('Product Value in R$ : '))

d10 = value*10/100
d = value-d10
portion = d/3
cvv = d*5/100
vp = value*5/100

print('You will pay this with a 10 percent of discount a value equals R$ %.2f' % d)
print(f'If you prefer, you can pay 3 portions with a value equals {portion}, \n during 3x with no interest.')
print(f'the seller will receive R${cvv} if client pays it in cash.')
print(f'If the client wants to pay it on portion (3x), the seller will receive {vp}')
