from datetime import date
atual =date.today().year
nascimento = int(input('Informe o seu Ano de Nascimento: '))
idade = atual - nascimento
if idade <=9:
    print('O atleta possuí {} anos.'.format(idade))
    print('Classificado como MIRIM')
elif idade <=14:
    print('O atleta possuí {} anos.'.format(idade))
    print('Classificado como INFANTIL')
elif idade <=19:
    print('O atleta possuí {} anos.'.format(idade))
    print('Classificado como JÚNIOR')
elif idade <=25:
    print('O atleta possuí {} anos.'.format(idade))
    print('Classificado como SÊNIOR')
else:
    print('O atleta possuí {} anos.'.format(idade))
    print('Classificado como MASTER')