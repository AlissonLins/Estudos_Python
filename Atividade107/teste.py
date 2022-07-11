# Exercitando módulos em Python
from Atividade107 import moeda
preço = float(input('Digite o preço: R$'))
print(f'A metade de R${preço} é R${moeda.metade(preço)} ')
print(f'O dobro de {preço} é R${moeda.dobro(preço)} ')
print(f'Fazendo um aumento de 10% teremos o valor de R${moeda.aumentar(preço, 10)}')