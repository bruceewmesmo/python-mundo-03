
# EXERCICIO 089 - BOLETIM COM LISTAS COMPOSTAS

lista = []

while True:
    
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2)/2

    lista.append([nome,[n1,n2], media])

    r = str(input('Quer continuar? [s/n] '))
    if r in 'Nn':
        break

for i, a in enumerate(lista):
    print(f'Aluno nº{i}: Nome: {a[0]}, Média: {a[2]:.1f}')

while True:
    opc = int(input('Qual o número do aluno que quer ver: [999 termina] '))
    if opc == 999:
        break
    if opc <= len(lista)-1:
        print(f'Notas de {lista[opc][0]} são: {lista[opc][1]}')
