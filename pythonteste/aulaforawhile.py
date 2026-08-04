'''cont = 1
while True:
    print(cont, '-> ', end='')
    cont += 1
print(cont)
n= cont = 0
while cont <3:
    n= int(input(' Digite um numero: '))
    cont = cont +1
    cont = cont +1'''

n = s = 0
while True:
    n = int(input(' Digite um numero : '))
    if n == 999:
        break
    s+=n
#print(' a soma vale {}'.format(s))    
print(f'a soma vale {s}')