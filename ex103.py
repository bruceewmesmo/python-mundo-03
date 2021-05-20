
# EXERCICIO 103 - FICHA DO JOGADOR

def ficha(nome = '<desconhecido>', gol = 0):
    print(f'O jogador {nome} fez {gol} gols')

n = str(input('Digite o nome do jogador: '))
g = str(input('Digite o número de gols do jogador: '))

if g.isnumeric:
    g = int(g)
else:
    g = 0

if n.strip() == '':
    ficha(gol = g)
else:
    ficha(n,g)
