#Fazendo implementações e melhorando a atividade 61
print('=-'*15)
print('Gerador de P.A')
print('=-'*15)
primeiro = int(input('Qual será o primeiro termo? '))
razão = int(input('Qual a razão? '))
termo = primeiro 
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{}  ➝  '.format(termo), end='')
        termo += razão
        cont += 1
    print('Pause')
    mais = int(input('Quantos termos você quer mostrar mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))