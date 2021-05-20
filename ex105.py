
# EXERCICIO 105 - ANALISANDO E GERANDO DICIONÁRIOS

def notas(*n, situacao = False):
    """
    -> Funcao para analisar notas e situacao de alunos
    :param n: uma ou mais notas da turma
    :param situação: incluir ou não na saida a situaçao da turma
    :return: Retorno um dicionario com o total de notas, o maior, o menor e media das notas da turma
    """
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if situacao:
        if r['media'] >= 7:
            r['situação'] = 'APROVADO'
        elif r['media'] >= 5:
            r['situação'] = 'RECUPERAÇÃO'
        elif r['media'] < 5:
            r['situação'] = 'REPROVADO'
    return r

resp = notas(5.5,2.5,6,8,2, situacao=True)
print(resp)
help(notas)
