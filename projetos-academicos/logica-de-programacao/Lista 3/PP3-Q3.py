inicial = int(input("Digite o valor inicial: "))

quantidade = 0
soma = 0

for n in range(inicial, -1, -1):
    print(n)
    quantidade += 1
    soma += n

print("Quantidade de valores:", quantidade)
print("Soma dos valores:", soma)