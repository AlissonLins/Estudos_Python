# Formatando moedas em Python
from Atividade109 import moeda

preço = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(preço)} é {(moeda.metade)(preço, True)} ')
print(f'O dobro de {moeda.moeda(preço)} é {(moeda.dobro)(preço, True)} ')
print(f'Fazendo um aumento de 10% teremos o valor de {(moeda.aumentar)(preço, 10, True)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(preço, 13, True)}')