from os import close

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


def linha(tamanho = 42):
    return '~'*tamanho


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\33[33m{c}\33[m-\33[34m{item}\33[m')
        c += 1
    print(linha())
    escolha = leiaint('\33[32mSua opção: \33[m')
    return escolha 


def arquivoexiste(nome):
    try:
        a = open(nome,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criaraquivo(nome):
    try:
        a = open(nome,'wt+')
        a.close()
    except:
        print('Houve um erro ao criar o arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso')


def lerarquivo(nome):
    try:
        a = open(nome,'rt')
    except:
        print('Erro ao abrir o arquivo')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arquivo,nome = 'Desconhecido',idade = 0):
    try:
        a = open(arquivo,'at')
    except:
        print('Houve um erro na abertura do arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro ao escrever os dados.')
        else:
            print(f'Novo registro de {nome} adicionado')
        finally:
            a.close()

arq = 'cursoemvideo.txt'

if not arquivoexiste(arq):
    print('Arquivo não encontrado')    
    criaraquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas','Cadastrar uma nova pessoa','Sair do sistema'])
    if resposta == 1:
        lerarquivo(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema. Até logo!')
        break
    else:
        print('\33[31mErro! Digite uma opção válida!\33[m')
