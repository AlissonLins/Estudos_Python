# Validando entrada de dados em Python
def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        numero = str(input(msg))
        if numero.isnumeric():
            valor = int(numero)
            ok = True
        else:
            print('\033[0;31mErro! Por Favor, Tente Novamente.\033[m')
        if ok:
            break
    return valor       
# Programa principal
número = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {número}')