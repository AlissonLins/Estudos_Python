# Analisando e gerando Dicionários
def notas(*n, sit=False):
    """
    ↦ Função para analisar notas e situações de vários alunos.
    ↦ parametro n: uma ou mais notas dos alunos (São aceita várias notas)
    ↦ parametro sit(situação): Valor opcional, indicando se deve ou não adicionar na situação
    ↦ return: dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >7:
            r['situação'] = 'Boa'
        elif r['média'] >= 5:
            r['situação'] = 'Razoável'
        else:
            r['situação'] = 'Ruim'
    return r
    
# Programa principal
resposta = notas(7.5, 5.5, 10, sit=True)
print(resposta)
