# Valores únicos em uma lista
valor = list()
while True:
    num = int(input('Digite um valor: '))
    if num not in valor:
        valor.append(num)
        print('Valor Adicionado com sucesso.')    
    else:
        print('Valor duplicador não será adicionado.')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja Adicionar outro valor? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('='*30)
print(f'Os valores cadastrados foram {sorted(valor)}')