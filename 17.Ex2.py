# Dada uma matriz 3x3 com números inteiros, descubra qual
# é o maior valor dentro dela e informe exatamente
# em qual linha e coluna ele foi encontrado.

matriz = []

for i in range(3):
    linha =[]
    for j in range(3):
        numero =int(input('digite um numero: '))
    matriz.append(numero)

maior = max(max(linha))
maior_linha = 0
maior_coluna = 0

for linha in matriz:
   if matriz < maior:
     maior_linha = i
for coluna in matriz:
    if matriz < maior:
        maior_coluna = j

for matriz in range(len(matriz)):
    matriz.append('{maior_linha}{maior_coluna}')
    print(f'{maior}')