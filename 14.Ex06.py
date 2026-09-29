#Construa uma página/programa onde o usuário digitará o nome e o bairro de dez pessoas.
# O programa exibirá o nome e bairro das pessoas
#  em ordem alfabética.

cadastro = []
for i in range(4):
    nome = input('Digite um nome: ')
    bairro = input('Digite um bairro: ')
    cadastro.append([nome, bairro])
    # cadastro[i] = [nome, bairro]

# Opção 1 -> Ordenar pelo nome
cadastro.sort()

# Opção 2 -> Ordenar pelo bairro
cadastro.sort(key=lambda x: x[1])
