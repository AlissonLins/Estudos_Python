'''def título(txt):
    print('-' *30)
    print(txt)
    print('-' *30)
título('  Programação ')
título('  Aprendendo Python   ')
título('  Alisson Lins   ')'''
 
'''def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')
# Programa principal
soma(b=4, a=5)
soma(7, 2)'''

'''def contador(*números):
    tamanho = len(números)
    print(f'Foram enviados os valores {números} e no total são {tamanho} números.')
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)'''

'''def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1 
valores = [4, 2, 6, 6, 1, 9]
dobra(valores)
print(valores)'''

def soma(*valores):
    s = 0
    for num in valores:
        s += num
        print(f'Somando os valores {valores} temos {s}')
soma(5, 2)
soma(2, 5, 0)