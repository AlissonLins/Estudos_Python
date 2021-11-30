salário = float(input('Qual é o salário do  funcionário? R$'))
novo = salário + (salário* 15 / 100)
print('O funcionário que ganhava {:.2f}, com um aumento de 15%, passará a receber {:.2f}'.format(salário, novo))
