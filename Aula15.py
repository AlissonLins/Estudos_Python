'''nome = 'Alisson'
idade = 19 
print(f'O {nome} tem {idade} anos.')'''

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break  
    s += n
print('A soma dos valores vale {} '.format(s))