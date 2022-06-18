#Maior e menor valores em tupla
from random import randint
sorteador = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)
print(f'Os Valores sorteados foram: {sorteador}')
#for n in sorteador:
#    print(f'{n}', end='')
print(f'O maior valor sorteado foi {max(sorteador)}')
print(f'O menor valor sorteado foi {min(sorteador)}')
