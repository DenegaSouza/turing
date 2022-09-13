"""
1º - Crie uma variável recebendo o conceito de polimorfismo com o sinal de igual.  
2º - Crie uma função de impressão usando interpolação e aplique a variável de polimorfismo antes e depois da string cabeçalho adicione quebra de linha, ao final. 
3º - Crie um laço de repetição recebendo uma condição que irá executar apenas números pares esses números devem percorrer até 1500. 
4º - Crie uma função de impressão após laco com a descrição parabéns você conseguiu! 
5º - Crie uma função de impressão usando interpolação e aplique a variável de polimorfismo antes e depois da string utilize como rodapé, definindo o fim do laço repetição! 
"""

poli = '='*10
print(f'\n{poli} CABEÇALHO {poli}\n')   # INTERPOLAÇÃO

for c in range(0, 1501, 2):
    print(c)

print('Parabens, você conseguiu !')

print(f'\n{poli} RODAPÉ {poli}\n')   # INTERPOLAÇÃO
