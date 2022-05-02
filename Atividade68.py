# JOGO PAR OU IMPAR
from random import randint 
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador 
    tipo = ''
    while tipo not in 'PI':
        tipo = str(input('PAR OU ÍMPAR?')).strip().upper()[0]
    print(f'Você jogou {jogador} e o cumputador {computador}. O total de {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('YOU WIN! ')
            v += 1 
        else:
            print('YOU LOOSE!') 
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('YOU WIN! ')
            v += 1
        else:
            print('YOU LOOSE! ')
            break
print('Vamos jogar denovo.')
print (f'GAME OVER! Você venceu {v} vezes.')