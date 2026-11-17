# O sistema deve gerenciar uma matriz 3x3, onde cada
# linha representa um rack físico (Rack 0, Rack 1 e Rack 2) e 
# cada coluna representa um sensor
# de temperatura instalado (Sensor 0, Sensor 1 e Sensor 2).

# O programa deve preencher a matriz 3x3 com as temperaturas registradas em
# graus Celsius (valores do tipo float).

# Utilize um laço while para validar individualmente a entrada de cada sensor,
# aceitando apenas temperaturas contidas na faixa operacional entre 10.0C e
# 90.0C.

matriz = []
for i in range(3): # cada rack
    lista = []
    for j in range(3): # cada sensor
        temperatura = float(input(f'Digite a temperatura do Sensor {j} do Rack {i}: '))
        while not 10 < temperatura < 90:
            temperatura = float(input(f'Digite a temperatura do Sensor {j} do Rack {i}: '))
        lista.append(temperatura)
    matriz.append(lista)

# Para cada um dos três racks (linhas da matriz), o programa deve calcular e
# exibir a temperatura média dos sensores que o compõem.
# descubra a maior temperatura
# absoluta registrada em toda a matriz e exiba o seu valor juntamente com as
# coordenadas exatas da sua localização (número do rack/linha e número do
# sensor/coluna).
maior_linha = 0 # rack
maior_coluna = 0 # sensor
for i in range(3):
    soma = 0
    for j in range(3):
        soma += matriz[i][j]
        if matriz[i][j] > matriz[maior_linha][maior_coluna]:
            maior_linha = i
            maior_coluna = j
    print(f'Média temperatura Rack {i} {soma/3:.2f}')

for linha in matriz:
    for numero in linha:
        print(numero, end='\t')
    print()

print(f'Maior temperatura encontrada foi: {matriz[maior_linha][maior_coluna]}')
print(f'No Rack {maior_linha} sendo no sensor {maior_coluna}')

if matriz[maior_linha][maior_coluna] > 75:
    print("ALERTA: Ponto Crítico de Sobreaquecimento Detectado")
