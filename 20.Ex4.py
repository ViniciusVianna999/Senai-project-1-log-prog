# Exercício 4: Mapeamento Condicional de Vetor
# Construa um programa que receba 8 números inteiros e os guarde em um vetor. Em
# seguida, crie um segundo vetor de mesmo tamanho no qual os números ímpares do
# vetor original sejam multiplicados por 2 e os números pares permaneçam
# inalterados. Ao final, exiba os dois vetores.

import copy

lista = []
for i in range(8):
    numero = int(input('Digite um número: '))
    lista.append(numero)

# forma 1 de criar uma cópia da lista
nova_lista = lista.copy() # copia (rasa)

for i in range(len(lista)):
    if lista[i] % 2 != 0: # se o número for ímpar
        nova_lista[i] = lista[i] * 2 # multiplica por 2
        # nova_lista[i] *= 2 # outra forma de fazer a mesma coisa

print(lista)
print(nova_lista)
 
# forma 2 ->   copiar on-the-fly (na hora)
nova_lista = [] 

for numero in lista:
    if numero % 2 != 0:
        nova_lista.append(numero * 2)
    else:
        nova_lista.append(numero)
print(lista)
print(nova_lista)

#forma 3 ->