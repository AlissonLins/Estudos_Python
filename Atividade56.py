#Leitor de nome, idade e sexo.
somaidade = 0
m = 0
maioridhomem = 0
namevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('==== {}ª Pessoa ===='.format(p))
    name = str(input('Nome: ')).strip()
    id = int(input('Idade: '))
    gen = str(input('Sexo [M/F/NB]: ')).strip()
    somaidade += id
    if p == 1 and gen in 'Mm':
        maioridhomem = id
        namevelho = name
    if gen in 'Mm' and id > maioridhomem:
        namevelho = name
    if gen in 'Ff' and id > 20:
        totmulher20 += 1
m = (id) /4
print('A média de idade do grupo é de {:.2f} anos'.format(m))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridhomem, namevelho))
print('Ao todo são {} mulher(es) com menos de 20 anos'.format(totmulher20))