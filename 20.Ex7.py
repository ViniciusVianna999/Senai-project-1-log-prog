# Desenvolva um módulo de console para auditar o consumo de combustível de
# veículos que retornam à base operacional ao longo de um turno de trabalho.

# O programa deve processar múltiplos veículos de forma contínua até
# que o operador digite 0 na quilometragem percorrida para sinalizar o
# fim do expediente.

# Para cada veículo válido,
# solicite a distância percorrida (em km) e a
# quantidade de combustível consumida (em litros). Utilize um laço while
# para validar que o volume de combustível seja estritamente maior que
# zero antes de prosseguir com o cálculo.

controle = True
# O total de veículos auditados;
# A quilometragem total acumulada pela frota;
# A média geral de consumo da frota no turno.
qtd_veiculos = 0
km_total = 0
media_geral = 0
while (True):
    km = float(input('Digite a quilometragem percorrida (0 para encerrar): '))
    if km <= 0:
       break
    litros = float(input('Digite a quantidade de litros consumidos: '))
    while (litros <= 0):
        litros = float(input('Digite a quantidade de litros consumidos: '))

    consumo = km / litros

    if consumo < 9:
        print('Alto Consumo')
    elif consumo >= 9 and consumo < 12:
        print('Consumo Moderado')
    else:
        print('Baixo Consumo')

    media_geral += consumo
    km_total += km
    qtd_veiculos += 1

print(f'total de veiculos: {qtd_veiculos}')
print(f'quilometragem total: {km_total}')
print(f'media geral: {media_geral / qtd_veiculos if qtd_veiculos > 0 else 0}')