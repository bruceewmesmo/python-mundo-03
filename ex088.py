
# EXERCICIO 088 - PALPITES PRA A MEGA SENA

from random import randint
lista = []
jogos = []
quantidade = int(input('Quantos jogos devem ser feitos? '))
total = 1

while total <= quantidade:
    cont  = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1

for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
