# Exercício 6: Multiplicação de Matriz por Escalar
# Desenvolva um programa que solicite o preenchimento de uma matriz 3 × 3 com
# números inteiros e, em seguida, peça ao usuário um valor numérico constante
# (escalar). Utilizando laços de repetição aninhados, o programa deve multiplicar cada
# elemento da matriz original por esse valor escalar e exibir a matriz resultante
# formatada em linhas e colunas.

matriz = []

for i in range(3): # linhas
    lista = []
    for j in range(3): # colunas
        numero = int(input('Digite um número: '))
        lista.append(numero) # guardo o que leio na coluna
    matriz.append(lista) # guardo a linha completa na matriz

escalar = int(input('Digite o numero inteiro: '))

for linha in matriz:
    for numero in linha:
        print(f'{numero * escalar}', end='\t') 
    print() # pular linha

    