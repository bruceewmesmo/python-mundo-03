
# EXERCICIO 098 - FUNÇAO CONTADOR

def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    elif passo == 0:
        passo = 1

    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont}', end = ' ')
            cont += passo
        print('Fim!')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont}', end = ' ')
            cont -= passo
        print('Fim!')

contador(1,10,1)
contador(10,0,2)
contador(1,42,-1)
