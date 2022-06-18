#Analise de dados em uma tupla
numero = (int(input('Digite o 1º número: ')),
        int(input('Digite o 2º número: ')),
        int(input('Digite o 3º número: ')),
        int(input('Digite o 4º número: ')))
print(f'Você digitou os valores {numero}')
print(f'O valor 9 apareceu {numero.count(9)} vezes.')
if 3 in numero:
    print(f'O valor 3 ficou na {numero.index(3)+1} posição.')
else:
    print('O valor 3 não foi digitado.')
print('Dos números digitados esses foram os valores pares: ', end=' ')
for n in numero:
    if n % 2 == 0:
        print(n, end=' ')
