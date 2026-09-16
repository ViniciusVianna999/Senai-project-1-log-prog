# Construa um programa onde o usuário digitará 
# um número e o programa completará o número
#  digitado até 0, apenas com números pares.

numero = int(input('Digite um numero: '))

for i in range (numero, -1, -1):
    if i % 2 == 0:
        print(i)