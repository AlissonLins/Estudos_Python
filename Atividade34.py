salário = float(input('Informe o salário do funcionário desejado: R$'))
if salário <= 1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)
print('Este funcionário ganhava R${:.2f} e passará a ganhar R${:.2f} agora.'.format(salário, novo))
