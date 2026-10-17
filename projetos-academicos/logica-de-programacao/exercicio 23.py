from xml.sax.saxutils import prepare_input_source

peso=83
altura=1.79
altura2=altura*altura
Imc=peso/altura2
print("Imc:",Imc)
if Imc>24.9: print("não sauldavel")
else : print("sauldavel")
