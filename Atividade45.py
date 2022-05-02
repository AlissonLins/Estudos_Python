#JOGO DE PEDRA, PAPEL E TESOURA
from random import randint
from time import sleep 
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções: 
[ 0 ] PEDRA 
[ 1 ] PAPEL 
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print("=" * 15)
print('computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('=' * 15)
if computador == 0: # COMPUTADOR JOGOU PEDRA
    if jogador == 0 :
        print('EMPATE')
    elif jogador == 1:
        print('PARABÉNS JOGADOR, VOCÊ GANHOU!')
    elif jogador == 2:
        print('HA HA, O COMPUTADOR VENCEU!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1: # COMPUTADOR JOGOU PAPEL
    if jogador == 0 :
        print('HA HA, O COMPUTADOR VENCEU!')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('PARABÉNS JOGADOR, VOCÊ GANHOU!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2: # COMPUTADOR JOGOU TESOURA 
    if jogador == 0 :
        print('PARABÉNS JOGADOR, VOCÊ GANHOU!')
    elif jogador == 1:
        print('HA HA, O COMPUTADOR VENCEU!')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')