
# EXERCICIO 082 - DIVIDINDO VALORES ENTRE LISTAS

lista = []
pares = []
impares = []

while True:
    
    lista.append(int(input('Digite um número: ')))
    r = str(input('Quer continuar? [s/n] '))
    if r in 'Nn':
        break

for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)

print(f'A lista completa é: {lista}')
print(f'A lista dos números pares é: {pares}'}
print(f'A lista dos números impares é: {impares}'}