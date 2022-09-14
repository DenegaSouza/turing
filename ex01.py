# Crie uma variável do tipo inteiro recebendo dados, então crie uma variável fazendo o cálculo do resto da divisão, usando máscara de substituição e realize 
# a atribuição do valor. Logo em seguida crie uma estrutura de condição onde irá imprimir no terminal se o cálculo da divisão é ímpar ou par;

idade = int(input("Qual a sua idade? "))

restoDaDiv = idade % 3

print("{}".format(restoDaDiv))

if (restoDaDiv%2) == 0:
     print("O resto da divisão é par")
        
else:
     print("O resto da divisão é ímpar")
