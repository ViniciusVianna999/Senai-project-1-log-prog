# Pegue o nome e a cidade
# se a cidade for RJ, print "Seja Bem-vindo a Cidade Maravilhosa, nome"
# Se não for RJ, exiba o nome da pessoa e da cidade


def verificar_local(nome, cidade):
    if cidade == "Rio de Janeiro" or cidade == "RJ":
        print(f'Seja Bem-vindo à Cidade Maravilhosa, {nome}')
    else:
        print(f'Seja Bem-vindo à {cidade}, {nome}')

nome = input("Digite seu nome: ")
cidade = input("Digite sua cidade: ")        

verificar_local(nome, cidade)

