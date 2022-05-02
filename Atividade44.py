#SIMULADOR DE PAGAMENTOS EM LOJA!

print('{:=^40}'.format(' LINS Empreendimentos '))
valor = float(input('Qual o valor das  Compras? R$ ')) 
print('Por Favor, Escolha uma forma de pagamento abaixo ⬇')
print('[ 1 ] Á Vista ')
print('[ 2 ] Á Vista no cartão ')
print('[ 3 ] Em até 2x no cartão ')
print('[ 4 ] 3x ou mais no cartão ')
escolha = int(input('Digite Aqui a sua escolha: '))
if escolha == 1 :
    total = valor - (valor * 10 / 100)
elif escolha == 2 :
    total = valor - (valor * 5 /100)
elif escolha == 3 :
    total = valor 
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R$ {:.2f}'.format(parcela))
elif escolha ==  4 :
    total = valor - (valor * 20 /  100)
    parcela = total / 3
    print('Sua compra será parcelada em 3x de R$ {:.2f}'.format(parcela))
else: 
    total = valor
    print('OPÇÃO DE PAGAMENTO INVÁLIDA, TENTE NOVAMENTE!')
print('Sua compra de {:.2f} vai custar {:.2f} no final. '.format(valor, total))