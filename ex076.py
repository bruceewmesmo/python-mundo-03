
# EXERCICIO 076 - LISTA DE PREÇOS COM TUPLA

lista = ('Arroz', 29.99,
         'Feijão', 8.00,
         'Açúcar', 3.59,
         'Sal', 2.35,
         'Azeite', 21.79)

print(f'{"LISTA DE COMPRAS":^30}')

for pos in range(0,len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<20}', end = '')
    else:
        print(f'R${lista[pos]:>6.2f}')