# Dividindo valores em várias listas
lista = []
pares = list()
ímpares = list()
while True:
    lista.append(int(input('Digite um número: ')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
for i, v in enumerate(lista): # Separação dos números pares em uma lista e dos ímpares em outra lista
    if v % 2 == 0:
        pares.append(v)
    else:
        ímpares.append(v)
print('='*30)
print(f'Os valores adicionados na lista foram: {lista}')
print(f'Os números pares da lista são: {pares}')
print(f'Os números ímpares da lista são: {ímpares}')
