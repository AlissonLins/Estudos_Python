nome = str(input('Qual é o seu nome? '))
if nome == 'Alisson':
    print('Belo nome!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana, Hope, Jéssica, Sophia':
    print('Que lindo nome!')
print('Tenha um excelente dia, {}!'.format(nome))