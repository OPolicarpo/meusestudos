#leia o nome completo de uma pessoa, mostrando o primeiro e o ultimo nome separadamente
n= str(input('digite seu nome completo ')).strip()
n1 = n.split()
print ('muuito prazer em te conhecer {}'.format(n))
print('seu primeiro nome e {}'.format(n1[0]))
print('seu ultimo nome e {}'.format(n1[len(n1)-1]))