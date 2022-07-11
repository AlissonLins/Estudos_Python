# Reduzindo ainda mais o programa
def aumentar(preço = 0, taxa = 0, formato = False):
    res = preço + (preço * taxa/100)
    return res if formato is False else moeda(res)

def diminuir(preço = 0, taxa = 0, formato = False):
    res = preço - (preço * taxa/100)
    return res if formato is False else moeda(res)
 
def dobro(preço = 0, formato = False):
    res = preço * 2
    return res if formato is False else moeda(res)

def metade(preço = 0, formato = False):
    res = preço / 2
    return res if formato is False else moeda(res)

def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')

def resumo(preço = 0, taxaA = 10, taxaR = 5):
    print('-'*30)
    print('Resumo do valor'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço \t{metade(preço, True)}')
    print(f'Com {taxaA}% de aumento: \t{aumentar(preço, taxaA, True)}')
    print(f'Com {taxaR}% de redução: \t{diminuir(preço, taxaR, True)}')
    print('-'*30)