"""Crie uma variável do tipo inteiro solicitando dados.
Crie uma variável recebendo o conceito de polimorfismo com o sinal de igual.
Crie uma função de impressão usando interpolação e aplique a variável de polimorfismo antes e depois da string cabecalho adicione quebra de linha, ao final.
Crie um laco de repeticao que execute o índice de contagem crescente até o número digitado pelo usuário
Crie uma função de impressão usando interpolação e aplique a variável de polimorfismo antes e depois do string utilize como rodapé."""

variavel = int(input("\nDigite um número: "))
titulo = "="*15 
rodape = "="*15

print(f"\n{titulo}\n CABEÇALHO \n{titulo}\n")


for x in range(0, variavel + 1):
    print(x)


print(f"\n{rodape}\n RODAPÉ \n{rodape}")