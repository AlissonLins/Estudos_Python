#Atividade 9 refeito em for
num = int(input('Digite um número para ver sua tabuada '))
for calc in range(1, 11):
    print('{} x {:2} = {}'.format(num, calc, num*calc))
 