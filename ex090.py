
# EXERCICIO 090 - DICIONÁRIO EM PYTHON

aluno = dict()
aluno['nome'] = str(input('Digite um nome: '))
aluno['média'] = float(input('Digite a média desse aluno: '))

if aluno['média'] >= 7:
    aluno['situação'] = 'aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'recuperação'
else:
    aluno['situação'] = 'reprovado'

print(f'O nome é {aluno["nome"]}')
print(f'A média é {aluno["média"]}')
for k,v in aluno.items():
    print(f'A {k} dele é {v}')
