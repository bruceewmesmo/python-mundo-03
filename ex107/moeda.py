def aumentar(preco,taxa):
    res = preco * (1 + taxa)
    return res


def diminuir(preco,taxa):
    res = preco * (1 - taxa)
    return res


def dobro(preco):
    res = preco * 2
    return res


def metade(preco):
    res = preco/2
    return res
    