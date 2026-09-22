# Construa um programa onde o usuario digitará 
# dez numeros e o programa
# somara e calculará a média dos numeros digitados.

lista = []
for i in range(0, 3):
    numero = float(input('Digite um número: '))
    lista.append(numero)

# soma = 0
# for item in lista:
#     soma = soma + item

media = sum(lista)/len(lista)
print(f'A média é: {media}')