# Formatando moedas em Python
from Atividade108 import moeda

preço = float(input('Digite o preço: R$'))
print(f'A metade de R${moeda.moeda(preço)} é {moeda.moeda(moeda.metade)(preço)} ')
print(f'O dobro de {moeda.moeda(preço)} é {moeda.moeda(moeda.dobro)(preço)} ')
print(f'Fazendo um aumento de 10% teremos o valor de R${moeda.moeda(moeda.aumentar)(preço, 10)}')