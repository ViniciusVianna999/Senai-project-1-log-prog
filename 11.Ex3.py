# Construa um programa onde o usuário digitará
#  cinco números e o programa deverá
#   colocar esses números dentro do vetor em ordem crescente.

numeros = []
n = int(input('Digite um número: '))


for i in range(0, 5):
    numero = int(input('Digite um número: '))
    numeros.append(numero)

numeros.sort()
print('crescente: ')
print(numeros)