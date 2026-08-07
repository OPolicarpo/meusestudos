'''crie um prorama onde o usuario digite uma expressao qualquer que use parenteses. 
seu aplicativo devera anilizar se a expressao passada esta com os parenteses abertos e fechados na ordem correta'''
''' essa e correcao eu nao consegui nem pensar como funcionaria a logica'''

expr = str(input('Digite a expressao: '))
pilha = []
for simb in expr:
        if simb == '(':
                pilha.append('(')
        elif simb == ')':
                if len(pilha)> 0:
                        pilha.pop()
if len(pilha) == 0:
        print ('Sua Expressao esta valida')
else: 
        print ('Sua expressao esta invalida')
