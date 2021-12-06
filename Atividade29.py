velocidade = float(input('Qual a velocidade atual do carro? '))
if velocidade >80:
    print('MUTADO! Vocë excedeu o limite de velocidade permitido que é 80Km/h')
    multa = (velocidade-80) * 7
    print('Você deverá pagar uma multa no valor de R${:.2f}!'.format(multa))
print('Tenha um Excelente dia! Dirija com Cuidado')
