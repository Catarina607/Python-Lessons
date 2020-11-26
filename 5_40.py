
cost_factory = float(input(' COST FACTORY U$S: '))


if cost_factory < 12.000:
    value = cost_factory + (cost_factory * (5/100))
    print(f'TOTAL COST US$: {value}')
elif cost_factory == 12.000 or cost_factory <= 25.000:
    value = cost_factory + (cost_factory + (10/100)) + (cost_factory *(15/100))
    print(f'TOTAL COST US$: {value}')
elif cost_factory > 25.000:
    value = cost_factory + (cost_factory * (15/100)) + (cost_factory * (20/100))
    print(f'TOTAL COST US$: {value}')
else:
    exit()
