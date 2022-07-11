# Transformando módulos em pacotes
def aumentar(preço = 0, taxa = 0, formato = False):
    '''
    ↠  Calcula o aumento de um determinado preço,
    retornando o resultado com ou sem formatação.
    Parametro preço: o preço que se quer reajustar
    Parametro taxa: qual é a porcentagem do aumento.
    Parametro formato: onde poderá escolher se deseja formatado ou não.
    return: o valor reajustado, com ou sem formato.
    '''
    res = preço + (preço * taxa/100)
    return res if formato is False else moeda(res)

def diminuir(preço = 0, taxa = 0, formato = False):
    '''
    ↠  Calcula a diminuição de um determinado preço,
    retornando o resultado com ou sem formatação.
    Parametro preço: o preço que se quer reajustar
    Parametro taxa: qual é a porcentagem do aumento.
    Parametro formato: onde poderá escolher se deseja formatado ou não.
    return: o valor reajustado, com ou sem formato.
    '''
    res = preço - (preço * taxa/100)
    return res if formato is False else moeda(res)
 
def dobro(preço = 0, formato = False):
    '''
    ↠  Calcula o dobro de um determinado preço,
    retornando o resultado com ou sem formatação.
    Parametro preço: o preço que se quer reajustar
    Parametro formato: onde poderá escolher se deseja formatado ou não.
    return: o valor reajustado, com ou sem formato.
    '''
    res = preço * 2
    return res if formato is False else moeda(res)

def metade(preço = 0, formato = False):
    '''
    ↠  Calcula a metade de um determinado preço,
    retornando o resultado com ou sem formatação.
    Parametro preço: o preço que se quer reajustar.
    Parametro formato: onde poderá escolher se deseja formatado ou não.
    return: o valor reajustado, com ou sem formato.
    '''
    res = preço / 2
    return res if formato is False else moeda(res)

def moeda(preço = 0, moeda = 'R$'):
    '''
    ↠  Calcula o aumento de um determinado preço,
    retornando o resultado com ou sem formatação.
    Parametro preço: o preço que se quer reajustar
    Parametro formato: onde poderá escolher se deseja formatado ou não.
    return: o valor reajustado, com ou sem formato.
    '''
    return f'{moeda}{preço:>.2f}'.replace('.', ',')

def resumo(preço = 0, taxaA = 10, taxaR = 5):
    '''
    ↠  Calcula o aumento de um determinado preço,
    retornando o resultado com ou sem formatação.
    Parametro preço: o preço que se quer reajustar
    Parametro taxa A: aumento na taxa no valor de 10%.
    Parametro taxa R: redução da taxa no valor de 5%.
    Parametro formato: onde poderá escolher se deseja formatado ou não.
    return: o valor reajustado, com ou sem formato.
    '''
    print('-'*30)
    print('Resumo do valor'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço \t{metade(preço, True)}')
    print(f'Com {taxaA}% de aumento: \t{aumentar(preço, taxaA, True)}')
    print(f'Com {taxaR}% de redução: \t{diminuir(preço, taxaR, True)}')
    print('-'*30)