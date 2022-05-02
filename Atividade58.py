# MELHORANDO O JOGO DA ATIVIDADE 28
from random import randint
from time import sleep
computador = randint(0, 10) #faz o computador "Pensar"
print('Olá, Sou o seu computador... Acabei de pensar em um número. Dica: entre 0 a 10. ')
print('Consegue acertar em qual número eu pensei? HA HA ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Em que número eu pensei? ')) #jogador deve adivinhar o número
    print('PROCESSANDO, AGUARDE...')
    sleep(1.5)
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Um pouco mais... tente outra vez.')
        elif jogador > computador:
            print('Um pouco menos... tente outra vez.')
print('PARABÉNS! Você me venceu, mas foram necessário {} Tentativas.'.format(palpites))