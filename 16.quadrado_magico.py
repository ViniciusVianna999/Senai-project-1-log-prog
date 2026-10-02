# Construa um jogo Quadrado Mágico 3X3, no qual o usuário preencherá o
# vetor com números de um a nove (sem repetir números)
#  e a soma de todas as linhas, colunas e
#  diagonais será igual a quinze.

# iniciar a maatriz com o que o usuario digitar(matriz 3x3)
matriz = []
for i in range(3): # 3 linhas
    linha = [] # iniciar a linha vazia
    for j in range(3): # 3 colunas
        numero = int(input(f'Digite o número entre 1 e 9: '))
        # validar se o numero está entre 1 e 9
        while numero <1 or numero >9:
            numero = int(input(f'Digite o número entre 1 e 9: '))
        
        linha.append(numero) # guardar o numero na linha

    matriz.append(linha) # guardar a linha na matriz
# forma 1 
soma = 0 # soma de cada linha, coluna e diagonal
somas = [] # guardar as somas de cada linha, coluna e diagonal

# verificar as linhas
for linha in matriz:
    soma = 0
    for numero in linha:
        soma += numero
    somas.append(soma)

# verificar as colunas
for j in range(3): # trava as colunas para 'andar' nas linhas
    soma = 0 # cria uma variavel para somar os numeros da coluna
    for i in range(3):  # isso é para andar nas linhas
        soma += matriz[i][j]
    somas.append(soma)

# verificar as diagonais
diagonal_principal = 0 # soma da diagonal principal
for i in range(3): # 
    diagonal_principal += matriz[i][i] 
somas.append(diagonal_principal)

diagonal_secundaria = 0 # soma da diagonal secundaria
for i in range(3):
    diagonal_secundaria += matriz[i][2-i]
somas.append(diagonal_secundaria)

# verificar se todas as somas são iguais a 15
if all(soma == 15 for soma in somas):
    print("É um Quadrado Mágico!")
else:
    print("Não é um Quadrado Mágico.")