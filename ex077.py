
# EXERCICIO 077 - CONTANDO VOGAIS EM TUPLAS

palavras = ('eu', 'nao', 'sei', 'pogramar',  'em',
            'python', 'mas',  'estou',  'tentando')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end = '')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end = ' ')
