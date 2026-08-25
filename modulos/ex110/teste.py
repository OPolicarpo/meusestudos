import moeda

p = float(input('Digite um preco: R$ '))
print(f'A metade de {moeda.moeda(p)} e {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} e {moeda.dobro(p, True)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(p,15, True)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p,13, True)} ')