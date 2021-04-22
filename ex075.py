
# EXERCICIO 075 - ANALISE DE DADOS EM UMA TUPLA

num = (int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')))

print(f'Os valores digitados foram {num}')

if 9 in num:
    print(f'O número 9 pareceu {num.count(9)}x')
else:
    print('O número 9 não foi digitado.')

if 3 in num:
    print(f'O número 3 apareceu na posição {num.index(3)}')
else:
    print('O número 3 não foi digitado.')

print('Os valores pares digitados foram:', end = ' ')
for n in num:
    if n % 2 == 0 and n != 0:
        print(n, end = ' ')