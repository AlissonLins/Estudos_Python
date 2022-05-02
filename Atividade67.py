#Refazendo atividade 9 com while and brake
while True:
    num = int(input('Qual Tabuada o Sr(a) deseja? '))
    if num < 0:
        break 
    print('='*30)
    for c in range(1, 11):
       print(f'{num} x {c} = {num*c} ')
    print('='*30)
print('Programa Finalizado. Volte Novamente!')