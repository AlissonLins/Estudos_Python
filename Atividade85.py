# Lista com pares e impares
numeros = [[], []]
valores = 0
for c in range(1, 8):
    valor = int(input('Informe sete valores: '))
    if valores % 2 == 0:
        numeros[0].append(valores)
    else:
        numeros[1].append(valores)
print('='*39)     
numeros[0].sort()
numeros[1].sort()
print(f'Os valores pares digitados acima foram: {numeros[0]}')
print(f'Os valores impares digitados acima foram: {numeros[1]}')