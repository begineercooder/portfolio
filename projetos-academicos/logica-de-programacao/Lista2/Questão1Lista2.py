ct=0
soma=0
counter20=0
print("Digite um numero negativo para sair")
while True:
    numero=float(input("Digite um numero real positivo: "))
    if numero <0:
        break
    ct=ct+1
    soma=soma+numero
    media=soma/ct
    if numero>20:
        counter20=counter20+1
print("quantidade de numeros digitados: ",ct)
print("Soma dos numeros digitados: ",soma)
print("A media dos numeros digitados: ",media)
print("Numeros digitados maiores que 20:",counter20)