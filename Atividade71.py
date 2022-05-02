#CAIXA ELETRÔNICO
print('='*26)
print('       BANCO LUBANK')
print('='*26)
valor = int(input('Quanto você deseja sacar? R$ ' ))
total = valor 
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Um total  de {totcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd == 10
        elif céd == 10:
            céd == 5
            totcéd = 0
        if total == 0:
            break
print('='*26)
print('OBRIGADO POR USAR O LUBANK! Tenha um ótimo dia!')