
# EXERCICIO 084 - LISTA COMPOSTA E ANALISE DE DADOS

temp = []
lista = []
maior = menor = 0

while True:
    
    temp.append(str(input('Digite um nome: ')))
    temp.append(int(input('Digite um peso: ')))
    if len(lista) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    lista.append(temp[:])
    temp.clear()
    
    r = str(input('Quer continuar? [s/n] '))
    if r in 'Nn':
        break

print(f'\nVocê cadastrou {len(lista)} pessoas.')
print(f'O maior peso foi: {maior}kgs.  Peso de: ')
for p in lista:
    if p[1] == maior:
        print(f'{p[0]}', end = ' ')

print(f'\nO menor peso foi: {menor}kgs.  Peso de: ')
for p in lista:
    if p[1] == menor:
        print(f'{p[0]}', end = ' ')
