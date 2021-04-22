
# EXERCICIO 073 - TUPLAS COM TIMES DE FUTEBOL

times = ('América-MG', 'Athletico-PR', 'Atlético-GO', 'Atlético-MG', 'Bahia', 'Bragantino',
        'Ceará', 'Chapecoense', 'Corinthians', 'Cuiabá', 'Flamengo', 'Fluminense', 'Fortaleza',
        'Grêmio', 'Internacional', 'Juventude', 'Palmeiras', 'Santos', 'São Paulo', 'Sport')

print(f'Os cinco primeiros são {time[:5]}')
print(f'Os quatro últimos são {time[-4:]}')
print(f'Os times em ordem alfabetica {sorted(times)}')
print(f'O Chapecoense está em {times.index("Chapecoense")} posição')
