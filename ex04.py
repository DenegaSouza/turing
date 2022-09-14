
#8º - Crie uma função de impressão usando interpolação e aplique a variável de polimorfismo antes e depois da string cabeçalho início estrutura de decisão adicione quebra de linha, 
# ao final.
#9º - Crie uma estrutura de decisão falando se a soma desses números é maior que 10, menor que 10, igual a dez, diferente de 10.
#10º - Crie uma função de impressão usando interpolação e aplique a variável de polimorfismo antes e depois da string utilize como rodapé, definindo o fim da estrutura de decisão.

variavel1 = 0

cabecalho = "="*15
rodape = "="*15

print(f"\n{cabecalho} \nCABEÇALHO\n{cabecalho}\n")

for x in range(1,4):
    numero = float(input(f"Digite {x}º número: "))
    variavel1 += numero

print("\nA soma dos valores é {}".format(variavel1))

print(f"\n{rodape} \nRODAPÉ\n{rodape}\n")

print(f"\n{cabecalho} \nCABEÇALHO\n{cabecalho}\n")

if variavel1 > 10:
    print("O número é diferente e maior que 10")

elif variavel1 < 10:
    print("O número é diferente e menor que 10")

else:
    print("O número é igual a 10")

print(f"\n{rodape} \nRODAPÉ\n{rodape}\n")