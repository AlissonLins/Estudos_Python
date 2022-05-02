n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2) /2 
print('Tirando {} e {}, a sua média foi {:.2f}'.format(n1, n2, m))
if m < 5.0:
    print('Você foi REPROVADO, estude mais!')
elif m >= 5.0:
    print('Você ficou em RECUPERAÇÃO!')
elif m <= 6.9:
    print('Você ficou em RECUPERAÇÃO!')
else:
    print('Você foi APROVADO!')