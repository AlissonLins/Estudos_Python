'''def função():
    n1 = 4 
    print(f'N1 dentro vale {n1}')
n1 = 2
função()
print(f'N1 fora vale {n1}')'''

'''def somar(a=0, b=0, c=0):
    s = a + b + c
    return s
r1 = somar(3, 2 ,5)
r2 = somar(2, 2)
r3 = somar(6)
print(f'Os resultados foram {r1}, {r2} e {r3}') '''

'''def fatorial(numero=1):
    f = 1
    for c in range(numero, 0, -1):
        f *= c
    return f
n = int(input('Informe um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')'''

''' def fatorial(numero=1):
    f = 1
    for c in range(numero, 0, -1):
        f *= c
    return f 
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}.')'''

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False
numero = int(input('Informe um número: '))
if par(numero):
    print('Este número é par! ')
else:
    print('Este número é impar! ')