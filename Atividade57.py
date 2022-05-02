#VALIDAÇÃO DE DADOS
'''sexo = 'M' 
while sexo == 'M':
    r = str(input('Por Favor, Informe o seu Sexo: [M/F] ')).upper().strip()[0]
    if r != sexo:
        print('Opção Inválida! Por Favor, tente novamente.')
    elif r :
        print('Sexo {} registrado com Sucesso!'.format(r))'''

sexo = str(input('Por Favor, Informe o seu Sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MF': 
    sexo = str(input('Opção Inválida, Por Favor, tente novamente.')).strip().upper()[0]
print('Sexo {} registrado com Sucesso!'.format(sexo))