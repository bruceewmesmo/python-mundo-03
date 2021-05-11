
# EXERCICIO 092 - CADASTRO DE TRABALHADOR EM PYTHON

from datetime import datetime

CTPS = {}
CTPS['trabalhador'] = str(input('Digite o nome do trabalhador: '))
CTPS['idade'] = datetime.now().year - int(input('Digite o ano de nascimento: '))
CTPS['n_carteira'] = int(input('Número da CTPS [0 se não possuir]: '))
if CTPS['n_carteira'] != 0:
    CTPS['contratação'] = int(input('Ano de contratação: '))
    CTPS['salario'] = float(input('Digite o salário: '))
    CTPS['aposentadoria'] = CTPS['idade'] + (CTPS['contratação'] + 35) - datetime.now().year

for k, v in CTPS.items():
    print(f'- {k} tem o valor de {v}')
