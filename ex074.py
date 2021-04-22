
# EXERCICIO 074 - 

from random import randint

num = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))

print('Os valores sorteados foram:', end= ' ')
for n in num:
    print(f'{n}', end = ' ')

print(f'\n O maior número sorteado foi {max(num)} e o menor {min(num)}')
