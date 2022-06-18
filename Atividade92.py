# Cadastro de Trabalhador em Python
from datetime import datetime
dados_usuarios = dict()
dados_usuarios['Nome'] = str(input('Nome: '))
nascimento =  int(input('Ano de Nascimento: '))
dados_usuarios['idade'] = datetime.now().year - nascimento
dados_usuarios['Carteira de Trabalho'] = int(input('Carteira de Trabalho (digite 0 caso não possua): '))
if dados_usuarios['Carteira de Trabalho'] != 0 :
    dados_usuarios['Contratação'] = int(input('Informe o Ano da contratação: '))
    dados_usuarios['Salário'] = float(input('Inforne o valor do seu salário: R$'))
    dados_usuarios['Aposentadoria'] = dados_usuarios['idade'] + ((dados_usuarios['Contratação'] + 35) - datetime.now().year)
print('='*40)
print(f'- Seu nome é {dados_usuarios["Nome"]} ')
print(f'- Tem {dados_usuarios["idade"]} ')
print(f'- Ctps é {dados_usuarios["Carteira de Trabalho"]} ')
print(f'O Ano de contratação foi em {dados_usuarios["Contratação"]} ')
print(f'Com o valor do salário em R${dados_usuarios["Salário"]} ')
print(f'Você poderá se aposentar com {dados_usuarios["Aposentadoria"]} anos. ')