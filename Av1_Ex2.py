# Desenvolva um programa em Python que leia 10 números inteiros e os 
# armazene em um vetor original. 
# A partir dessa estrutura, crie duas novas listas independentes: 
# uma lista denominada pares, contendo cada número par do vetor original 
# multiplicado por 3, e uma lista denominada ímpares,
# contendo os números ímpares mantidos com seus valores inalterados. 
# Ao final, o programa deve exibir o vetor original, os dois novos 
# vetores resultantes e a contagem exata de elementos alocados em cada um deles.

lista = []
for i in range(10):
    numero = int(input('Digite um valor: '))
    lista.append(numero)

pares = []
impares = []

for numero in lista:
    # verificar se é par
    if numero % 2 == 0:
        pares.append(numero*3)
    # caso contrario, é impar
    else:
        impares.append(numero)

print(f'Lista Original: {lista}; tamanho: {len(lista)}')
print(f'Lista dos Pares: {pares}; tamanho: {len(pares)}')
print(f'Lista dos Impares: {impares}; tamanho: {len(impares)}')