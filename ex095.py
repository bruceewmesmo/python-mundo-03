
# EXERICIO 095 - APRIMORANDO OS DICIONÁRIOS
time = []
jogador = {}
partidas = []

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome: '))
    tot = int(input('Número de partidas jogadas: '))
    partidas.clear()
    for c in range(0,tot):
        partidas.append(int(input(f'Quantos gols na partida {c+1}: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    r = str(input('Continuar[S/N]: ')).strip().upper()
    if r in 'N':
        break

for k,v in enumerate(time):
    print(f'{k:<3}', end = ' ')
    for d in v.values():
        print(f'{str(d):<15}', end = ' ')
    print()

while True:
    busca = int(input('Quer ver melhor qual jogador: [999 para] '))
    if busca == 999:
        break
    if busca >= len(time):
        print('Número de jogador inválido!')
    else:
        print(time[busca]['nome'])
        for i, g in enumerate(time[busca]['gols']):
            print(f'No jogo {i+1} fez {g} gols')

print('Finalizando...')
