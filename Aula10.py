#nome = str(input('Qual o seu nome? '))
#if nome == 'Gustavo':
    #print('Que nome lindo você tem!')
#else: 
    #print('Seu nome é tão normal')
#print('Bom dia, {}!'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota:'))
m = (n1 + n2)/2
print('A sua média foi {:.2f}'.format(m))
if m >6.0:
    print('PARABÉNS! Você passou com a nota acima da média!')
if m == 6.0:
    print('PARABÉNS! Você passou arrasto mas passou. HAHA')
else:
    print('Sua nota não atingiu a média necessária, Estude mais!')