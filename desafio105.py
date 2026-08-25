'''faca um programa que tenha uma funcao notas que pode receber varias notas de alunos
e vai retornar um dicionario com as seguintes informacoes:
quantidade de notas / a maior nota / a menor nota/ a media da turma /
 a sutuacao atual (opicional)
 adicione as docstrings.'''

def notas(*n, sit=False):
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media']>= 7:
            r['situacao'] = 'boa'
        elif r['media'] >=5 :
            r['situacao'] = 'razoavel'
        else:
            r['situacao'] = 'ruim'
    return r
    

#programa principal
resp = notas (5.5, 2.5, 0, sit=True)
print(resp)
