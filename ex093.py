
# EXERCICIO 093 - CADASTRO DE JOGADOR DE FUTEBOL

infos = {}
partidas = []
infos['nome'] = str(input('Nome do jogador: '))
n_partidas = int(input('Quantas partidas ele jogou: '))

for c in range(0,n_partidas):
    partidas.append(int(input(f'Número de gols na partida {c+1}: ')))

infos["total"] = sum(partidas)

print(f'O nome do jogador é {infos["nome"]}')
for partida, gols in enumerate(partidas):
    print(f'Na partida {partida+1} {infos["nome"]} fez {gols} gols')
print(f'Com um total de {infos["total"]} de gols')
