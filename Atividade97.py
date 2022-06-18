# Um print especial
def temas(mensagem):
    tamanho = len(mensagem) + 4
    print('-' * tamanho)
    print(f'  {mensagem}')
    print('-' * tamanho)
# Programa principal
temas('Alisson Lins')
temas('Aln')
temas('Programador Júnior')