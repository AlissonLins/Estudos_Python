# Jogo de Dados em Python
from random import randint
from time import sleep
from operator import itemgetter
jogos = {'O Jogador 1': randint(1, 6),
         'O Jogador 2': randint(1, 6),
         'O Jogador 3': randint(1, 6),
         'O Jogador 4': randint(1, 6)}
ranking = list()
print('Os Valores sorteados: ')
for k, v in jogos.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1.5)
print('='*45)
print('== RANKING GLOBAL ==')
ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'   {i+1} lugar: {v[0]} com {v[1]}.')
    sleep(1.5)