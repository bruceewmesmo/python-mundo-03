import moeda

p = float(input("Digite o preço: R$ "))

print(f'A metade do preço é {moeda.metade(p, formato = True)}')
print(f'O dobro do preço é {moeda.dobro(p, formato = True)}')
print(f'O preço com adicional de 10% é {moeda.aumentar(p,0.1, formato = True)}')
print(f'O preço com desconto de 10% é {moeda.diminuir(p,0.1, formato = True)}')
