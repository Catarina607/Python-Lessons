
print('=====================================')
print('    T A X       C A L C U L A T E R ')
print('=====================================')
print('Choice A States: ')
print('MG')
print('SP')
print('RJ')
print('MS')
state = input('Which One State: ')
value = float(input('Write a Value R$: '))


if state == 'MG' or state.lower() == 'mg':
    mgt = value * 0.7
    tmg = mgt + value
    print('-----------------------------')
    print('STATE:              MG')
    print(f'Value            R${value}')
    print(f'TAX: 7%   =     R${mgt}')
    print(f'TOTAL:           R${tmg}')
    print('------------------------------')
elif state == 'SP' or state.lower() == 'sp':
    spt = value * 0.12
    tsp = spt + value
    print('-----------------------------')
    print('STATE:              SP')
    print(f'Value            R${value}')
    print(f'TAX: 12%   =    R${spt}')
    print(f'TOTAL:           R${tsp}')
    print('------------------------------')
elif state == 'RJ' or state.lower() == 'rj':
    rjt = value * 0.15
    rjg = rjt + value
    print('-----------------------------')
    print('STATE:              RJ')
    print(f'Value            R${value}')
    print(f'TAX: 15%   =    R${rjt}')
    print(f'TOTAL:           R${rjg}')
    print('------------------------------')
elif state == 'MS' or state.lower() == 'ms':
    mst = value * 0.8
    tms = mst + value
    print('-----------------------------')
    print('STATE:               MS')
    print(f'Value             R${value}')
    print(f'TAX: 8%   =      R${mst}')
    print(f'TOTAL:            R${tms}')
    print('------------------------------')
else:
    print('Invalid Sintaxe')
