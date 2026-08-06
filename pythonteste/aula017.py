num = [2, 5 , 9, 1]
num[2]=3
num.append(7)
num.sort(reverse=True)
num.insert(2,2)
if 4 in num:
    num.remove(4)
else:
    print('nao achei o numero 4')
num.remove(2)#soremove o promeiro elemento
print(num)
print(f'Essa lista tem {len(num)} elementos')