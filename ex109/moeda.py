def aumentar(preco = 0,taxa = 0, formato = False):
    res = preco * (1 + taxa)
    return res if formato is False else moeda(res)


def diminuir(preco = 0,taxa = 0, formato = False):
    res = preco * (1 - taxa)
    return res if formato is False else moeda(res)


def dobro(preco = 0, formato = False):
    res = preco * 2
    return res if formato is False else moeda(res)


def metade(preco = 0, formato = False):
    res = preco/2
    return res if formato is False else moeda(res)


def moeda(preco, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')
