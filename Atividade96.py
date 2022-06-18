# Função que calcula área
from time import sleep
def área(largura, comprimento):
    a = largura * comprimento
    print(f'A área de um terreno de {largura}x{comprimento} é de {a}m²')
# Programa principal
print('    Controle de Terreno')
print('-'*28)
larg = float(input('Informe a largura (m):'))
sleep(1)
compri = float(input('Informe o comprimento (m): '))
área(larg, compri)