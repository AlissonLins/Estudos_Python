# Lista composta e análise de dados
registro = list()
dados = list()
totalpessoas = maiorpeso = menorpeso =  0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(registro) == 0 :
        maiorpeso = menorpeso = dados [1]
    else:
        if dados[1] > maiorpeso:
            maiorpeso = dados[1]
        if dados[1] < menorpeso:
            menorpeso = dados[1]
    dados.clear()
    registro.append(dados[:])
    totalpessoas += 1
    resp = ' '
    while resp not in 'S/N':
            resp = str(input('Deseja continuar? ')).strip().upper()[0]
    if resp == 'N':
        break
print('='*48)
print(f'Ao todo foram cadastradas um total de {totalpessoas} pessoas.')
'''for p in registro :
    if p[1] == maiorpeso:
        print({p[0]})'''
print(f'O maior peso foi de {maiorpeso}Kg. ')
print(f'O menor peso foi de {menorpeso}Kg. ')