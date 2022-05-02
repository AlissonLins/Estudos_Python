nmr = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para fazer a conversão ')
print('[ 1 ] converter para BINÁRIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')
opção = int(input('Qual base deseja converter: '))
if opção == 1 :
    print('{} convertido em BINÁRIO é igual a {}'.format(nmr, bin(nmr)[2:]))
elif opção == 2 :
    print('{} convertido em OCTAL é igual a {}'.format(nmr, oct(nmr)[2:]))
elif opção == 3 :
    print('{} convertido em HEXADECIMAL é igual a {}'.format(nmr, hex(nmr)[2:]))
else:
    print('Opção inválida, Tente novamente.')