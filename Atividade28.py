from random import randint
from time import sleep
computador = randint(0, 5) #faz o computador "Pensar"
print('-_-' *20)
print('Vou pensar em um numero entre 0 e 5, Tente adivinhar...')
print('-_-' *20)
jogador = int(input('Em que número eu pensei? ')) #jogador deve adivinhar o número
print('PROCESSANDO, AGUARDE...')
sleep(1.5)
if jogador == computador:
    print('PARABÉNS! Você me venceu, Legal!')
else:
    print('Eu Venci! HAHAHA, Eu pensei no número {} e não no número {}!'.format(computador, jogador))
