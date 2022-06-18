# Unindo dicionários e listas
dados_dos_usuários = dict()
total_usuarios = list()
soma = média = 0
while True:
    dados_dos_usuários.clear
    dados_dos_usuários['Nome'] = str(input('Nome do usuário: '))
    dados_dos_usuários['Idade'] = int(input('Idade do usuário: '))
    soma += dados_dos_usuários['Idade']
    while True:   
        dados_dos_usuários['Sexo'] = str(input('Informe o sexo [M/F] ')).upper()[0]
        if dados_dos_usuários['Sexo'] in 'MF':
            break
        print('Erro! Por Favor, Tente Novamente.')
        total_usuarios.append(dados_dos_usuários.copy())
    while True:
        resposta = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if resposta in 'SN':
            break
        print('Erro! Por Favor, Tente Novamente.')
    if resposta == 'N':
        break
print('='*30) # Até aqui leitura dos dados inseridos pelos usuários.
print(f'No total foram cadastradas {len(total_usuarios)} pessoas.') # Analisando e mostrando resultado dos dados fornecidos 
média = soma / len(total_usuarios)
print(f'A média de idade é de {média:5.2f} anos.')
print(f'As mulheres cadastradas foram ', end='')
for p in total_usuarios:
    if p['Sexo'] in 'Ff':
        print(f'{p["Nome"]}', end='')
print()
print('D) Lista das pessoas que estão acima da média: ', end='')
for p in total_usuarios:
    if p['Idade'] >= média:
        print('  ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('>>> Programa encerrado <<<')