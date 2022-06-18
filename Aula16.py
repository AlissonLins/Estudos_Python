#Tuplas
#Tuplas são imutaveis
lanche = 'Hambúrger', 'Suco', 'Pizza', 'Pudim'
#for cont in range(0, len(lanche)):
#    print(f'eu vou  comer {lanche[cont]}')

#for comida in lanche:
    #print(f'Eu vou comer {comida}')
    
for pos, comida in enumerate(lanche):
    print(f'eu vou comer {comida} na posição {pos}')
print('Comi o suficiente, estou cheio.')