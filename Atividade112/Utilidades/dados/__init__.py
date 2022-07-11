def leia_dinheiro(msg):
    válido = False
    while not válido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mErro! \"{entrada}\" é um valor inválido!\033[m')
        else:
            válido = True 
            return float(entrada)
