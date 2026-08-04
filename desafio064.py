''' Escreva um programa que leia varios numeros inteiros pelo teclado. o programa so vai parar quando o 
usuario digitar 999, que e a condicao de parada. no final mostre quantos numeros foram digitados e a soma entre eles
desconsiderando a flag '''
n = 0
cont = 0
soma = n 
n1 = 0
while n1 != 999:
    n1 = int(input(' Digite um numero: ')) 
    cont = cont+ 1
    soma = soma + n1
print(cont - 1)
print (soma - 999)