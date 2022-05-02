#Leitor de Nascimento
from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0
for c in range(1, 8):
    data = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    idade = atual - data
    if idade >= 18:
       totalmaior += 1
    else:
       totalmenor -= 1
print('Ao todo tivemos {} pessoas maiores de idade.'.format(totalmaior))
print('E {} menores de idade.'.format(totalmenor))