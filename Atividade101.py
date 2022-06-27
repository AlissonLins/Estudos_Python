# Funções para votação
def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: o voto não é obrigatório. ' 
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: o voto é opcional. '
    else:
        return f'Com {idade} anos o voto é obrigatório. '
# Programa Principal
nascimento = int(input('Por Favor, informe o ano de nascimento: '))
print(voto(nascimento))