quantidade = 0

print("Múltiplos de 3 até 21:")
for n in range(1, 22):
    if n % 3 == 0:
        print(n)
        quantidade += 1

print("Quantidade de valores:", quantidade)