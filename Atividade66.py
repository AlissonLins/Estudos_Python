#Leitor de números inteiro
n = s = c = 0
while True:
    n = int(input('Digite um número [999 para encerrar]: '))
    if n == 999:
        break
    c += 1
    s += n
print('A soma dos {} valores foi {}'.format(c, s))