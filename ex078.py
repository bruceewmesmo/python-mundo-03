
#EXERCICIO 078 - MAIOR E MENOR VALOR NA LISTA

lista = []

for i in range(0,5):
    lista.append(int(input(f'Digite um número na posição {i}: ')))

min = min(lista)
max = max(lista)

print(f'O menor número é {min} nas posições: ', end = '')
for i, v in enumerate(lista):
    if v == min:
        print(i,end='... ')

print(f'\nO maior número é {max} nas posições: ', end = '')
for i, v in enumerate(lista):
    if v == max:
        print(i,end='... ')
