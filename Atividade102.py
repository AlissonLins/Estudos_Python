# Função para Fatorial
def fatorial(n, show=True):
    """
    ↦ Calcula o Fatorial de um número.
    :parametro n: O número a ser calculado.
    :parametro show: (opcional) mostra ou não a conta.
    :return: O valor do fatorial de um número (n).
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f
# Programa principal
#print(fatorial(5, show=True))
help(fatorial)