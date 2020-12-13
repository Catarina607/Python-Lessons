print('       ESTATÍSTICA DA LIGHT      ')
print('-------------------------------------')
habit = float(input('Habitantes: '))
kwh = float(input('$$ KWH: '))
print('---------------------------------')
maior = menor = media = c = soma = res = com = ind = 0
p = 's'.upper().lower()
while p == 's'.upper().lower():
    print('  [1] - Residencial')
    print('  [2] - Comercial')
    print('  [3] - Industrial')
    cc = int(input('CODIGO DO CONSUMIDO: '))
    cons_m = float(input('CONSUMO DO MÊS $$$ : '))
    print('-------------------------------------')
    p = input('Posso continuar ?[S/N]:')
    c += 1
    soma = soma + cons_m
    media = (soma*kwh)/c
    if c == 1:
        maior = menor = cons_m
    else:
        if cons_m > maior:
            maior = cons_m
        if cons_m < menor:
            menor = cons_m
    if cc == 1:
        res = cons_m
    if cc == 2:
        com = cons_m
    if cc == 3:
        ind = cons_m
    if p == 'n'.upper().lower():
        break
print('--------------------------------------------')
print('              DADOS COLETADOS              ')
print('-------------------------------------------')
print('Média consumo $$$:  {} | '.format(round(media, 2)))
print('Maior consumo $$$:  {} | '.format(round(maior*kwh, 2)),  end='')
print('Menor consumo $$$:  {} | '.format(round(menor*kwh)))
print('  --------------------------------')
print(' |             CONSUMO             |')
print('  --------------------------------')
print(' RESIDENCIAL {}        | \n'.format(round(res*kwh, 2)))
print(' COMERCIAL {}          | \n'.format(round(com, 2)))
print(' INDUSTRIAL {}         | \n'.format(round(ind*kwh, 2)))