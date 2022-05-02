# Contador de números pares com soma
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite um número: '.format(c)))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print('Os números PARES informados no total são {} e a soma deles é {} '.format(cont, soma))
