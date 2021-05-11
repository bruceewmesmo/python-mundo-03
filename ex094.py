
# EXERCICIO 094 - UNINDO DICIONARIOS E LISTAS

lista_pessoas = []
pessoa = {}
soma = media = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    
    pessoa['idade'] = int(input('Idade: '))
    while pessoa['idade'] <= 0:
        pessoa['idade'] = int(input('Idade inválidade! Digite a idade: '))
    
    pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
    while pessoa['sexo'] not in 'MF':
        pessoa['sexo'] = str(input('Sexo inválido! Sexo [M/F]: ')).upper()
    soma += pessoa['idade']

    lista_pessoas.append(pessoa.copy())

    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resposta in 'N':
        break
    if resposta not in 'NS':
        resposta = str(input('Resposta inválida! Quer continuar? [S/N] ')).strip().upper()

print(lista_pessoas)

print(f'{len(lista_pessoas)} pessoas foram cadastradas')
media = soma/len(lista_pessoas)
print(f'A média de idade é {media} anos')
print()
print('As mulheres cadastradas foram:', end = ' ')
for p in lista_pessoas:
    if p['sexo'] in 'F':
        print(f'{p["nome"]}', end = ' ')
print()
print('As pessoas cadastradas com idade acima da média foram:', end = ' ')
for p in lista_pessoas:
    if p['idade'] >= media:
        print(f'{p["nome"]}', end = ' ')
