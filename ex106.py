
# EXERCICIO 106 - INTERACTIVE HELPING SYSTEM  IN PYTHON
cores = (
    '\033[m', # 0 - sem cor
    '\033[0;30;41m', # 1 - vermelho
    '\033[0;30;43m', # 2 - amarelo
    '\033[0;30;45m' # 3 - roxo
);

def ajuda(com):
    titulo(f'Acessando o manual do comando\'{com}\'',3)
    help(com)

def titulo(msg,cor = 0):
    tam = len(msg)+4
    print(cores[cor], end = '')
    print('~'* tam)
    print(f'  {msg}')
    print('~'* tam)
    print(cores[0])

comando = ''
while True:
    titulo('Sistema de Ajuda PyHelp', 1)
    comando = str(input('Função ou biblioteca: '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)

titulo('Até logo',2)
