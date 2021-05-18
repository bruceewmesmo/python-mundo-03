
# EXERCICIO 100 - FUNÇÕES PARA SORTEAR E SOMAR

from random import randint

def sorteia(lista):
    for cont in range(0,5):
        lista.append(randint(1,10))
    print(lista)


def somaPar(lista):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(soma)


lista = []
sorteia(lista)
somaPar(lista)
