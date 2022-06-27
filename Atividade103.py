# Ficha do Jogador
def ficha(nome='<Desconhecido>', gol=0):
    print('='*45)
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato. ')
# Programa principal
nome = str(input('Informe o nome do jogador: '))
gols = str(input('Informe quantos gols o jogador fez: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(gol=gols)
else:
    ficha(nome, gols)
