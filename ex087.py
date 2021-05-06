
# EXERCICIO 087 - MAIS SOBRE MATRIZ EM PYTHON

matriz = [[0, 0, 0],
       [0, 0, 0],
       [0, 0, 0]]

soma_par = maior = soma_col = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor na posição [{l}:{c}]: '))

for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            soma_par += matriz[l][c]

for l in range(0,3):
    soma_col += matriz[l][2]

for c in range(0,3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]


print(f'A soma dos pares é: {soma_par}')
print(f'A soma dos valores da 3ª coluna foi: {soma_col}')
print(f'O maior valor na segunda coluna é {maior}')
