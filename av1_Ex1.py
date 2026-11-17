# Construa um programa em Python que solicite 6 números inteiros ao usuário e 
# os armazene em uma lista. Em seguida, percorra a lista para calcular a média 
# aritmética de todos os valores informados e determinar a quantidade de números 
# pares presentes. Ao final da execução, o programa deve exibir a lista completa, 
# o valor da média calculada e o total de elementos pares encontrados.

# parte 1
lista = []
for i in range(6):
    numero = int(input('Digite um número: '))
    lista.append(numero)

# verificar quantos são pares
pares = 0
# soma = 0
# contador = 0
for numero in lista:
    if numero % 2 == 0: # significa que é par
        pares += 1
    # soma += numero
    # contador += 1

# media2 = soma / contador
media = sum(lista) / len(lista)

print(f'Lista Completa: {lista}\nMedia: {media:.2f}\nQtd. de Pares: {pares}')