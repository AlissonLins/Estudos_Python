#Refazendo a atividade 51 com while
print('=-'*15)
print('Gerador de P.A')
print('=-'*15)
primeiro = int(input('Qual será o primeiro termo? '))
razão = int(input('Qual a razão? '))
termo = primeiro 
cont = 1
while cont <= 10:
    print('{}  ➝  '.format(termo), end='')
    termo += razão
    cont += 1
print('Acabou!')