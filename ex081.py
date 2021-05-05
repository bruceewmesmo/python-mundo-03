
# EXERCICIO 081 - EXTRAIR DADOS DE UMA LISTA

lista = []

while True:
    
    lista.append(int(input('Digite um número: ')))

    r = str(input('Quer continuar? [s/n] '))
    if r in 'Nn':
        break

print(f'Você digitou {len(lista)} valores')
lista.sort(reverse = True)
print(f'A lista em ordem decrescente foi: {lista}')
if 5 in lista:
    print('O valor 5 está na lista.')
else:
    print('O valor 5 não está na lista')
