# Tendo uma matriz numérica 3x3:
# substitua múltiplos de 3 por Fus;
# substitua múltiplos de 5 por Ro;
# substitua múltiplos de 3 e de 5 por Dah.

matriz = []
for i in range(3):
    linha = [0,0,0]
    for j in range(3):
        numero = int(input('Digite um numero: '))
    matriz.append(linha)
def regras(valor):
    if valor % 3 == 0 and valor % 5 == 0:
        print ("Dah")
    if valor % 3 == 0:
        print("fus")
    if numero %5 == 0:
        print("Ro")
    else:
        print(f"{numero}")

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        matriz[i][j] = regras(matriz[i][j])

print('resultado: ')

for linha in matriz:
    print(linha)
    
     