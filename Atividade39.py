from datetime import date
atual = date.today().year
print('[ 1 ] converter para MASCULINO')
print('[ 2 ] converter para FEMININO')
print('[ 3 ] converter para NÃO-BINARIO')
sexo = str(input('Esolha um gênero acima ↑ :'))
nasc = int(input('Digite o seu ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18 :
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18 :
    saldo = 18 - idade
    print('Ainda faltam {} anos para o seu alistamento'.format(saldo))
    ano = atual + saldo 
    print('Seu alistamento será em {}'.format(ano))
else :
    idade > 18 
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))
