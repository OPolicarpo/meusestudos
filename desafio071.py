'''Crie um programa que simule o funcionamento de um CAIXA ELETRONICO
no inicio pergunte ao usuario qual sera o valor sacado(inteiro)
e o programa vai informar quantas cedulas de cada valor serao entregues.
considere que o caixa pussui 50/20/10/1'''
valor = int(input(' Qual valor deseja sacar: '))
total = valor
ced = 50
totced=0
while True:
    if total >= ced:
      total-=ced
      totced +=1
    else:
        if totced>0:
          print(f'Total de {totced} notas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced ==20:
            ced=10
        elif ced ==10:
           ced = 1
        totced = 0
        if total ==0:
           break
