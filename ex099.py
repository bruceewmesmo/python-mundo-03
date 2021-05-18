
# EXERCICIO 099 - FUNÇÃO QUE DESCOBRE O MAIOR

def maior(*num):
    cont = maior = 0
    for n in num:
        if cont == 0 or n > maior:
            maior = n
        cont += 1
    print(f'Foram digitados {cont} números e o maior foi {maior}')

maior(2,6,7,3,5,7)
maior(0,4,63,2)
maior(1,2,3)
maior()
