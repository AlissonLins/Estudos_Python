totcompra = totprodutos = menor = cont = 0
barato = ''
while True:
    print('-'*26)
    print('     Lojas Super Galax')
    print('-'*26)
    produto = str(input('Nome do Produto:'))
    preço = float(input('Preço: R$ '))
    cont += 1
    totcompra += preço
    if preço > 1000:
        totprodutos += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer Continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total da sua compra foi de R${totcompra:.2f}')
print(f'No total foram cerca de {totprodutos} itens que custaram mais de R$1000.00')
print(f'O produto mais barato foi {barato} no valor de R${menor:.2f} ')