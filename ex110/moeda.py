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

def moeda(preco= 0, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')

def resumo(preco=0, taxa_aumento=10, taxa_reducao=5):
    print(f'Preço analisado: \t\t{moeda(preco)}')
    print(f'O dobro de {moeda(preco)} é \t\t{dobro(preco,True)}')
    print(f'A metade de {moeda(preco)} é \t\t{metade(preco,True)}')
    print(f'{moeda(preco)} com taxa de aumento é \t{aumentar(preco,taxa_aumento,True)}')
    print(f'{moeda(preco)} com taxa de redução é \t{diminuir(preco,taxa_reducao,True)}')