tot18 = toth = totmulher20 = 0
while True:
    print('==== CADASTRO DE PESSOAS ====')
    id = int(input('Qual a sua idade? '))
    sexo = ' '
    while sexo not in 'MFNB':
        sexo = str(input('Sexo [M/F/NB]: ')).strip().upper()[0]
    if id >= 18:
        tot18 += 1
    if sexo == 'M':
        toth += 1
    if sexo == 'F' and id < 20:
        totmulher20 += 1 
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja Continuar [S/N]')).upper().strip()[0]
    if resp == 'N':
        break     
print(f'Ao todo existem {tot18} pessoas com mais de 18 anos.')
print(f'Ao todo foram cadastrados {toth} homens.')
print(f'E temos ao todo {totmulher20} mulher com menos de 20 anos.')