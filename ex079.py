
# EXERCICIO 079 - VALORES ÚNICOS EM UMA LISTA

lista = []

while True:
    num = int(input('Digite um número: '))
    if num not in lista:
        lista.append(num)
    else:
        print(f'O número {num} já existe na lista')
    
    continuar = str(input('Quer continuar? [S/N] '))
    if continuar in 'Nn':
        break

print(lista)
