# Cadastro de Jogador de Futebol
dados_do_jogador = dict()
partidas = list()
total = 0
dados_do_jogador['Nome'] = str(input('Qual o nome do jogador? '))
dados_do_jogador['partidas'] = int(input(f'Quantas partidas {dados_do_jogador["Nome"]} participou? '))
for c in range(0, total):
    partidas.append(int(input(f'    Quantos gols na {c+1}º partida')))
    total += 1
dados_do_jogador['Gols'] = partidas[:]
dados_do_jogador['total'] = sum(partidas)
print('='*40)
print(dados_do_jogador)
print('='*40)
for k, v in dados_do_jogador.items():
    print(f'O campo {k} tem o Valor {v}')
print('='*40)
print(f'O jogador {dados_do_jogador["Nome"]} jogou {len(dados_do_jogador["Gols"])} partidas.')
for i, v in enumerate(dados_do_jogador['Gols']):
    print(f'    Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {dados_do_jogador["total"]} gols.')