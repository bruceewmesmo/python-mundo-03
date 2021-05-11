
# EXERCICIO 091 - JOGO DE DADO EM PYTHON

from random import randint
from operator import itemgetter

jogo = {'Jogador 01': randint(1,6),'Jogador 02': randint(1,6),'Jogador 03': randint(1,6),'Jogador 04': randint(1,6)}


for jogador, lançamento in jogo.items():
    print(f'O {jogador} tirou {lançamento} no dado')

jogo_ordenado = sorted(jogo.items(), key = itemgetter(1), reverse = True)

print('=-'*20)
for i, v in enumerate(jogo_ordenado):
    print(f'O {i+1}º lugar: {v[0]} com {v[1]}')
