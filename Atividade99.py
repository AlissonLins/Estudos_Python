# Função que descobre o maior
from time import sleep
def maior(*num):
    cont = maior = 0
    print('='*28)
    print('Analisando os valores informados...')
    for valor in num:
        print(f'{valor} ',end='', flush=True)
        sleep(1)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} números no total.')
    print(f'O maior número informado foi {maior}.')
# Programa principal
maior(2, 9, 5, 3, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()