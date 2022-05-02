#CALCULADOR DE IMC
peso = float(input('Por Favor, Informe o seu peso atual: '))
altura = float(input('Por Favor, Informe sua altura atual: '))
IMC = peso / (altura ** 2)
if peso <= 18.5:
    print('O seu Indece de Massa é {:.1f}'.format(IMC))
    print('Você está abaixo do Peso')
elif peso >= 18.5:
     print('O seu Indece de Massa é {:.1f}'.format(IMC))
     print('Você está no Peso Ideal')
elif peso <= 25:
     print('O seu Indece de Massa é {:.1f}'.format(IMC))
     print('Você está no Peso Ideal')
elif peso >=25:
     print('O seu Indece de Massa é {:.1f}'.format(IMC))
     print('Você está com Sobrepeso')
elif peso <=30:
    print('O seu Indece de Massa é {:.1f}'.format(IMC))
    print('Você está com Sobrepeso')
elif peso >=30:
    print('O seu Indece de Massa é {:.1f}'.format(IMC))
    print('Você está com Obesidade')
elif peso <=40:
    print('O seu Indece de Massa é {:.1f}'.format(IMC))
    print('Você está com Obesidade')
else:
    print('O seu Indece de Massa é {:.1f}'.format(IMC))
    print('Você está com Obesidade Mórbida')