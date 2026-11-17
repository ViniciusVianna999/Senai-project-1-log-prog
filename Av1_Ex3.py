# Construa um programa em Python que receba os dados para preencher uma matriz 3x3 
# com números inteiros informados pelo usuário. Após o preenchimento, o sistema 
# deve solicitar um valor numérico de corte (limiar). O programa deve varrer a 
# matriz, contabilizar quantos elementos são estritamente maiores que esse limiar 
# e gerar uma segunda matriz 3x3 onde todos os valores superiores ao limiar sejam 
# substituídos por 0, mantendo os demais inalterados. Ao final, exiba a contagem 
# de elementos acima do limiar e a matriz resultante formatada em linhas e colunas.

# ler a entrada
matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        numero = int(input('Digite um valor: '))
        linha.append(numero)
    matriz.append(linha)

# o sistema deve solicitar um valor numérico de corte (limiar).
limiar = int(input('Digite um valor de corte: '))

# contar quantos numeros da matriz são maiores que o limiar
contador = 0
# guardar uma nova matriz
import copy
nova_matriz = copy.deepcopy(matriz)

for i in range(len(matriz)): # quantas linhas tem a tabela
    for j in range(len(matriz[i])): # quantos elementos tem na linha atual
        if matriz[i][j] > limiar:
            contador += 1
            nova_matriz[i][j] = 0
        else:
            nova_matriz[i][j] = matriz[i][j]

print(f'Qtd. de Valores Maior que o Limiar: {contador}')
for linha in nova_matriz:
    for numero in linha:
        print(numero, end='\t')
    print()


# Forma 2 -> criando nova matriz on-the-fly (na hora)

# nova_matriz = []
# contador = 0
# for linha in matriz:
#     nova_linha = []
#     for numero in linha:
#         if numero > limiar:
#             nova_linha.append(0)
#             contador += 1
#         else:
#             nova_linha.append(numero)
#     nova_matriz.append(nova_linha)