'''teste = list()
teste.append('Alisson')
teste.append(19)
galera = list()
galera.append(teste[:])
teste[0] = 'Lins'
teste[1] = 20
galera.append(teste[:])
print(galera)'''

'''galera = [['João', 19], ['Anna', 19], ['Joaquim', 13], ['Maísa', 18]]
for p in galera :
    print(f'{p[0]} tem {p[1]} anos de idade')'''

galera = list()
dados = list()
totalmaior = totalmenor = 0
for c in range(0, 5):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()

for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade.')
        totalmaior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totalmenor += 1
print(f'Temos {totalmaior} maiores e {totalmenor} menores de idade.')