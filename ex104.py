
# EXERCICICO 104 - VALIDANDO ENTRADA DE DADOS NO PYTHON

def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('Erro! Digite um número.')
            ok = False
        if ok:
            break
    return valor

n = leiaint('digite um número: ')
print(n)
