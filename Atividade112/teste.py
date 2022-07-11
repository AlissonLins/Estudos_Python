from Atividade112.Utilidades import moeda
from Atividade112.Utilidades import dados
preço = dados.leia_dinheiro('Digite o preço: R$')
moeda.resumo(preço, 20, 12)