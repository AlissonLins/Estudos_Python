'''pessoas = {'nome': 'Alisson', 'Sexo': 'M', 'Idade': 19}
print(f'O {pessoas["nome"]} tem {pessoas["Idade"]} anos')
print(pessoas.items())
pessoas['peso'] = 63.7
for k, v in pessoas.items():
    print(f'{k} = {v}')'''

brasil = []
estado1 = {'Uf': 'Bahia', 'sigla': 'BA'}
estado2 = {'Uf': 'São paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]['Uf'])