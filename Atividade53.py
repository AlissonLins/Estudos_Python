#Leitor de frases 'para saber se é um palindromo'
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
   inverso += junto[letra]
print('O inverso da frase {} é {}'.format(junto, inverso))
if inverso == junto :
    print('Essa frase é um palíndromo!')
else:
    print('Essa frase não é um palíndromo!')