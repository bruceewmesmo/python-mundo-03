import moeda

p = float(input("Digite o preço: R$ "))

print(f'A metade do preço é R${moeda.metade(p):.2f}')
print(f'O dobro do preço é R${moeda.dobro(p):.2f}')
print(f'O preço com adicional de 10% é R${moeda.aumentar(p,0.1):.2f}')
print(f'O preço com desconto de 10% é R${moeda.diminuir(p,0.1):.2f}')
