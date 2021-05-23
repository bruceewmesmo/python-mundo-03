
# EXERCICIO 113 - FUNÇÕES APROFUNDADAS EM PYTHON

def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError,TypeError):
            print('\33[31mERRO! Digite um número inteiro válido.\33[m')
            continue
        except KeyboardInterrupt:
            print('\33[31mEntrada de dados interrompida\33[m')
            return 0
        else:
            return n

def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError,TypeError):
            print('\33[31mERRO! Digite um número real válido.\33[m')
            continue
        except KeyboardInterrupt:
            print('\33[31mEntrada de dados interrompida\33[m')
            return 0
        else:
            return n

num1 = leiaint('Digite um valor inteiro: ')
num2 = leiafloat('Digite um valor real: ')
