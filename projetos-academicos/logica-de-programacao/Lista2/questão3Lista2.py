print("aperte 0 para sair")
numerosPares=0
contadorPares=0
numerosImpares=0
contadorImpares=0
while True:
    numero=int(input("Digite um número: "))
    if numero==0:
        break

    if numero%2==0:
        numerosPares=numerosPares+numero
        contadorPares=contadorPares+1
    else:
        numerosImpares=numerosImpares+numero
        contadorImpares=contadorImpares+1
if contadorPares>0:
    mediaPares=numerosPares/contadorPares
else:
    mediaPares=0
if contadorImpares>0:
    mediaImpares=numerosImpares/contadorImpares
else:
    mediaImpares=0
contadorTotal=contadorPares+contadorImpares
numerosTotal=numerosPares+numerosImpares
print("A media dos ", contadorPares," números pares é: ", mediaPares)
print("A media dos ", contadorImpares," números ímpares é: ", mediaImpares)
print("A quantidade de números totais digitados é: ", contadorTotal)
print("A soma de todos os números digitados é: ", numerosTotal)