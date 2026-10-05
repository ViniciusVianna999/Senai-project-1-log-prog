matriz = [] # Inicializa a matriz vazia

print("Digite os valores da matriz 3x3:") # saida para o usuário
for i in range(3): # Itera sobre as linhas da matriz
    linha = [] # Inicializa a linha vazia
    for j in range(3): # Itera sobre as colunas da matriz
        valor = int(input(f"Digite o valor para a posição [{i}][{j}]: ")) 
        # Solicita ao usuário que digite o valor para a posição [i][j]
        linha.append(valor) # Adiciona o valor digitado à linha
    matriz.append(linha) # Adiciona a linha completa à matriz

# Exibe a matriz digitada
print("\nMatriz digitada:") # saida para o usuário
for linha in matriz: # Itera sobre cada linha da matriz
    print(linha) # Exibe a linha da matriz

# Encontra o maior valor
maior = matriz[0][0] # Inicializa o maior valor com o primeiro elemento da matriz
linha_maior = 0 # Inicializa a linha do maior valor
coluna_maior = 0 # Inicializa a coluna do maior valor

for i in range(3): # Itera sobre as linhas da matriz
    for j in range(3): # Itera sobre as colunas da matriz
        if matriz[i][j] > maior: # Verifica se o valor atual é maior que o maior valor encontrado até agora
            maior = matriz[i][j] # Atualiza o maior valor
            linha_maior = i # Atualiza a linha do maior valor
            coluna_maior = j # Atualiza a coluna do maior valor

print(f"\nMaior valor: {maior}") # saida para o usuário
print(f"Encontrado na linha {linha_maior} e coluna {coluna_maior}") # saida para o usuário
print(f"Posição (1-based): linha {linha_maior + 1}, coluna {coluna_maior + 1}") # saida para o usuário