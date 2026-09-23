# Construa um programa onde o usuário digitará sete números 
# e o programa escreverá, na tela
# , quantos deles são pares e quantos são ímpares.

lista =['1', '2', '3', '4', '5', '6','7']
pares = 0
impares = 0

for i in range (0, 7):
    numero = int(input('Digite um numero: '))
    lista.append(numero)
    i += 1

    if numero % 2 == 0:
        pares += 1
    else: 
        impares += 1
print('Pares: ', pares)
print('impares: ', impares)