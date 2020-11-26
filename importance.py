
print('---------------------------------')
print('   C  A  L  C  U  L  A  T  E  R  ')
print('---------------------------------')

value = 780.000
dw1 = 46*value/100
print('The first winner receives R$ %.3f' % dw1)
rv = value-dw1
# print('it remains R$ %.3f' % rv)
dw2 = 36*rv/100
print('The 2th winner receives R$ %.3f ' % dw2)
nn_v = rv-dw2
print('the 3th winner receives R$ %.3f' % nn_v)
