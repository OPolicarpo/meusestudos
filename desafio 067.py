'''faca um programa que mostre a taboada de varios numeros, um de cada vez,
para cada valor digitado pelo usuario
o programa sera interrompido quano o numero for negativo'''

n = int(input(' Quer ver a taboada de qual valor? '))
while  True:
    if n <0:
        break
    cont = 0
    while cont <10:
        cont += 1
        r = n * cont
        print  (f'{n} x {cont} ={r}')
    n = int(input(' Quer ver a taboada de qual valor? '))   
print('opcao invalida') 
