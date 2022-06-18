#Boletim com listas compostas
notas = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    notas.append([nome, nota1, nota2, media])
    resp = ' '
    while resp not in 'S/N':
        resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
            break
print('='*30)
print(f'{"Nº.":<4} {"Nome" :<10}{"Média":>8}')
print('='*30)
for i, a in enumerate(notas):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('='*30)
    opção = int(input('Deseja Visualizar as notas de qual aluno? (digite 9 para encerrar): '))
    if opção == 9:
        print('Finalizando aplicação...')
        break
    if opção <= len(notas) - 1:
        print(f'As notas de {notas[opção][0]} são {notas[opção][1]}')
print('Obrigado pela Utilização, Volte Sempre :) ')