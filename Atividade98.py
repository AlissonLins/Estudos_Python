# Função de Contador
from time import sleep
def contador(começo, final, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print('-'*28)
    print(f'Contando de {começo} até {final} de {passo} em {passo}')
    sleep(2.5)
    if começo < final:
        cont = começo
        while cont <= final:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += passo
        print('Fim!')
    else:
        cont = começo
        while cont >= final:
            print(f'{cont} ', end='',flush=True)
            sleep(0.5)
            cont -= passo
        print('Fim!')
# Programa principal 
contador(1, 10, 1)
contador(10, 0, 2)
print('-'*28)
print('Você agora irá criar uma contagem personalizada.')
inicio = int(input('Digite o inicio da sua contagem: '))
final= int(input('Digite o final da sua contagem: '))
passo = int(input('Digite a quantidade de passos da sua contagem: '))
contador(inicio, final, passo)