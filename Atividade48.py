# Calculadora de números multiplos de 3
soma = 0   
cont = 0
for calc in range(1, 501, 2):
    if calc % 3 == 0:
        soma = soma + calc
        cont = cont + 1
print('A soma de todos os {} valores adquiridos é igual a {}'.format(cont,soma))