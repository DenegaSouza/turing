variavel1 = int(input("Digite um número para calcular a tabuada até 10: "))

print("="*12, "Tabudada do número", variavel1, "="*12)
for x in range(1,11):
    print(x,"*",variavel1,"=", x * variavel1)

print("="*12, "Fim da tabudada do número", variavel1, "="*12)