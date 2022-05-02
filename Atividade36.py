valor = float(input('Qual o Valor da casa desejada: R$ '))
sálario = float(input('Qual a média salarial do comprador: R$ '))
financiamento = int(input('Será financiado em quantos anos? '))
prestação = valor / (financiamento * 12)
mínimo = sálario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos,'.format(valor, financiamento), end='')
print(' a prestação será de R${:.2f}'.format(prestação))
print('ANALISANDO EMPRÉSTIMO...')
if prestação <= mínimo:
    print('Empréstimo será LiBERADO')
else:
    print('Empréstimo NEGADO')
