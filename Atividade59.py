#sistema menu de opções
from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5 :
    print('[ 1 ] Somar ')
    print('[ 2 ] Multiplicar ')
    print('[ 3 ] Maior ')
    print('[ 4 ] Novos Números ')
    print('[ 5 ] Sair do programa ')
    sleep(1)
    opção = int(input('Escolha uma alternativa: '))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre os valores {} e {} é {} '.format(n1, n2, soma))
        sleep(3)
    elif opção == 2: 
        multi = n1 * n2
        print('A multiplicação entre os valores {} e {} é {}'.format(n1, n2, multi))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            print('Entre os valores {} e {} o maior número entre eles é {}'.format(n1, n2, maior))
    elif opção == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('FINALIZANDO...  ')
    else:
        print('Opção Inválida. Tente novamente.')
    print('=-=' * 10)
sleep(2)
print('Fim do programa! Volte Sempre!')