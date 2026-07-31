#aluguel de carros
qd= float(input('quantos dias corregam de locacao do veiculo? '))
km= float(input('quantos km ele rodou nesse tempo? '))
res=(qd*60) + (km * 0.15)
print(' o preco a pagar por {} dias e {} kilometros de locacao foi de {:.2f}'.format(qd,km,res))