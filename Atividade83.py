# Validando expressões matemáticas
expressão = int(input('Digite a expressão: '))
pilha = []
for símb in expressão:
    if símb == '(':
        pilha.append('(')
    elif símb == ')':
        if len(pilha) > 0:
            pilha.pop()
         # Sempre que um encontrar'(' será armazenado dentro da pilha  e quando encontrar ')' ou a lista está vazia ou ela esta cheia podendo o parenteses está no final da lista
        else:
            pilha.append(')')
            break # sai do for 
if len(pilha) == 0: # Verifica se a pilha está cheia ou não
    print('Sua expressão está válida!')
else:
     print('Sua expressão não é válida!')
