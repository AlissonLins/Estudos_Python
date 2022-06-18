# Palpites para a Mega Sena
from random import randint
from time import sleep
numeros = list()
jogos = list()
print('='*30)
print('      JOGA NA MEGA SENA')
print('='*30)
escolha = int(input('Quantos jogos você quer que eu sorteie? '))
total = 1
while total <= escolha:
    cont = 0
    while True:
        valores = randint(1, 61)
        if valores not in numeros:
            numeros.append(valores)
            cont += 1
        if cont >= 6:
            break
    numeros.sort()
    jogos.append(numeros[:])
    numeros.clear()
    total += 1
print(f'====== Sorteando {escolha} Jogos ======')
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1.5)
    print('====== < Boa Sorte! > ======')