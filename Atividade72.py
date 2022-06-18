# Número por extenso
escolha = 'S'
extenso = 'Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte'
while True:
    número = int(input('Digite um número entre 0 a 20: '))
    if 0 <= número <= 20: 
        break
    print('Tente novamente.', end='')
    escolha = str(input('Deseja Continuar? [S/N] ')).upper().strip()[0]
print(f'Você digitou o número {extenso[número]}') 
