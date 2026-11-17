# O sistema deve monitorar 5 máquinas utilizando vetores unidimensionais.
# deve preencher duas listas paralelas
# código numérico de identificação de cada máquina e
# outra contendo o respectivo consumo

cod_numerico = []
consumo_maquina = []
for i in range(5):
    # o sistema deve validar a entrada do consumo através de
    # um laço while, garantindo que o valor informado em kWh seja estritamente
    # maior que zero antes de passar para a máquina seguinte.
    codigo = int(input('Digite o codigo da maquina: '))
    consumo = float(input('Digite o consumo (KW/h) da maquina: '))

    while consumo <= 0: # while not consumo > 0:
        print('Entrada Inválida')
        consumo = float(input('Digite o consumo (KW/h) da maquina: '))

    cod_numerico.append(codigo)
    consumo_maquina.append(consumo)

# Solicite ao operador o valor do "Teto Operacional de Consumo" (número real
# único para a verificação de toda a linha industrial).
teto_op = float(input('Digite o teto operacional de consumo para validação: '))

# maior consumo
maior_indice = 0
maior_que_o_teto = False
for i in range(5):
    # Quais máquinas ultrapassaram o teto operacional, exibindo seu
    # código e o consumo registrado;
    if consumo_maquina[i] > teto_op:
        print('Máquina operando acima do teto operacional de consumo:')
        print(f'Máquina {cod_numerico[i]}; consumo: {consumo_maquina[i]}')
        maior_que_o_teto = True

    # O código e o consumo da máquina com o maior consumo absoluto da planta;
    if consumo_maquina[i] > consumo_maquina[maior_indice]:
        maior_indice = i


# A média aritmética de consumo de todas as 5 máquinas.
media = sum(consumo_maquina)/len(consumo_maquina)

print(f'A média de consumo das 5 máquinas é: {media:.2f} KWh')

if not maior_que_o_teto:
    print('Operação Dentro dos Parâmetros de Eficiência')