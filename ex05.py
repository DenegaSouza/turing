'''1º - Usando o conceito de importação otimizada importe a biblioteca que tem a capacidade de gerar um delay na impressão.
2º - Crie uma variável recebendo o conceito de polimorfismo com o sinal de igual.
3º - Crie uma função de impressão usando interpolação e aplique a variável de polimorfismo antes e depois da string cabeçalho
adicione quebra de linha, ao final.
4º - Usando o conceito de contagem regressiva crie um laço de repetição que exiba cada número do índice até 20, gere um delay
 de 2 segundos e imprima uma mensagem de Feliz dia do programador na sua aplicação console.
5º - Crie uma função de impressão usando interpolação e aplique a variável de polimorfismo antes e depois da string utilize
 como rodapé, definindo o fim do laço de repetição.
'''

from time import sleep

poli = "="*15

print(f"\n{poli} Cabeçalho {poli}\n")

for x in range (20, -1, -1):
    print(x)

sleep(2)

print("Feliz dia do programador!!!!")

print(f"\n{poli} Rodapé {poli}\n")
