
# EXERCICIO 097 - UM PRINT ESPECIAL

def print_especial(txt):
    t = len(txt)+4
    print('^'*t)
    print(f'  {txt}')
    print('^'*t)

print_especial('Curso em Vídeo')
print_especial('Amamos o Guanabara')
print_especial('Python é bom demais!')
