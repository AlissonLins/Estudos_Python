# Aprimorando os Dicionários
dados_do_jogador = dict()
partidas = list()
time = list()
while True:
    dados_do_jogador.clear()
    dados_do_jogador['Nome'] = str(input('Qual o nome do jogador? '))
    dados_do_jogador['partidas'] = int(input(f'Quantas partidas {dados_do_jogador["Nome"]} participou? '))
    partidas.clear()
    for c in range(0, ):
        partidas.append(int(input(f'    Quantos gols na {c+1}º partida')))
    dados_do_jogador['Gols'] = partidas[:]
    dados_do_jogador['total'] = sum(partidas)
    time.append(dados_do_jogador.copy())
    while True:
        resposta = str(input('Deseja coninuar? [S/N]')).upper()[0]
        if resposta in 'SN':
            print('Erro! Por Favor, Tente Novamente.')
        if resposta == 'N':
            break
print('='*40) # Leitura de varios jogadores diferentes 
print('Cod', end='') # Mostrando os resultados
for i in dados_do_jogador.keys():
    print(f'{i:<15}', end='')
print('='*40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('='*40)
while True:
    buscar = int(input('Mostrar os registro de dados de qual jogador? (Digite 999 para parar.)'))
    if buscar == 999:
        break
    if buscar >= len(time):
        print(f'ERRO! Não existe jogaador com este código {busca}!')
    else:
        print(f'-- Levantamento do jogador {time[bucsar]["Nome"]}:')
        for i, g in enumerate(time[busca]['Gols']):
            print(f'    No jogo {i+1} fez {g} gols')
    print('-'*40)
print('>>> Volte Sempre :) <<<')