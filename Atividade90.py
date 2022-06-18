# Dicionário em Python 
aluno = dict()
aluno ['nome'] = str(input('Informe o nome do aluno: '))
aluno ['média'] = float(input(f'Qual o Média de {aluno["nome"]}: '))
print(f'- O nome do aluno é {aluno["nome"]} ')
print(f'- A média dele(a) é {aluno["média"]}')
print('='*35)
if  aluno['média'] >= 7:
    print(f'- O(a) Aluno(a) {aluno["nome"]} está em Aprovado.')
elif 5 <= aluno['média'] < 7:
    print(f'- O(a) Aluno(a) {aluno["nome"]} está em recuperação.')
else:
    print(f'- O(a) Aluno(a) {aluno["nome"]} está Reprovado.')
print('='*35)