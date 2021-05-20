
# EXERCICIO 101 - FUNÇÕES PARA VOTAÇÃO

def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        print('Voto negado.')
    elif idade <= 18 or idade > 65:
        print('Voto opcional.')
    else:
        print('Voto obrigatório.')

voto(1993)
