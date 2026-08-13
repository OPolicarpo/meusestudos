''' faca um programa que leia o nome e a media de um aluno
guardando tambem a situacao em um dicionario. no final
mostr o conteudo da estrutura na tela, media acima de 7 aprovrado - abaixo reprovado''' 
aluno = dict()
aluno['nome'] = str(input('Digite seu nome:'))
aluno['nota'] = float(input('Digite sua media:'))
if aluno['nota']>= 7:
    aluno['media'] = 'Aprovado'
else :
    aluno['media'] = 'Reprovado'
#print(f'Nome: {aluno['nome']} ') 
print(f'Media de {aluno['nome']}: {aluno['nota']}')
print(f'Situacao atual e : {aluno['media']} ')