import moeda

p = float(input("Digite o preço: R$ "))

print(f'A metade do preço é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro do preço é {moeda.moeda(moeda.dobro(p))}')
print(f'O preço com adicional de 10% é {moeda.moeda(moeda.aumentar(p,0.1))}')
print(f'O preço com desconto de 10% é {moeda.moeda(moeda.diminuir(p,0.1))}')
