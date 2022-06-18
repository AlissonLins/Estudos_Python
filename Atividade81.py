# Extraindo dados de uma lista
valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('='*30)
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True) # Coloca os números em ordem decrescente
print(f'Os valores em orden decrescente são {valores}')
if 5 in valores :
    print('O Valor 5 faz parte da lista.')
else:
    print('Valor 5 não foi encontrado.')