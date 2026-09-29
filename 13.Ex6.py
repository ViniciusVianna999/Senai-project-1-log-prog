# Construa um programa que o usuário digitará o nome e a idade
# de dez pessoas e o programa escreverá o nome do usuário
# mais novo.

lista = []

for i in range(4):
    nome = input('Digite um nome: ')
    idade = int(input('Digite uma Idade: '))
    lista.append([nome, idade])

# Forma 1 -> Usar o indice (o mais novo esta no inicio da lista)
mais_novo = 0 # indice
[['eu', 50], ['tu', 70]]
# o loop inicia do próximo elemento
for i in range(1, len(lista)):
    if lista[i][1] < lista[mais_novo][1]: 
        mais_novo = i

print(f'O usuario mais novo é: {lista[mais_novo][0]}')

# forma 2 -> agora com a função min
[['Alfredo', 35], ['labubu', 5]]
mais_novo = min(lista, key= lambda pessoa: pessoa[1])
print(f'O usuario mais novo é: {mais_novo[0]}')