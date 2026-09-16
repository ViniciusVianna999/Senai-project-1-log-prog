# Construa uma página onde o usuário digitará um valor
#  e o programa mostrará, na tela, a tabuada de multiplicação
#  deste número.

numero = int(input('Dgite um número para ver sua tabuada: '))

for i in range(0,10):
    resultado = numero * (i + 1)
    print(f'{numero} x {i+1} = {resultado}')

i = 0 
while i <= 10:
    print(f'{numero} x {i} = {numero * i}')
    i+=1