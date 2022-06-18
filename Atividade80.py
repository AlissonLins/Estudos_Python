# Lista ordenada sem repetições
valores = list()
for v in range(0, 5):
    num = int(input('Digite um Valor: '))
    if v == 0 or num > valores[-1]:
        valores.append(num)
        print('Adicionado ao final da lista.')
    else:
        pos = 0
        while pos < len(valores):
            if num <= valores[pos]:
                valores.insert(pos, num)
                print(f'Adicionado na posição {pos} da lista.')
                break
            pos += 1
print('='*40)
print(f'Os valores digitados em suas ordens foram {valores}')