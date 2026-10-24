# Escreva um programa que solicite ao usuário 
# o nome de três alunos. O script deve salvar esses 
# nomes em um arquivo chamado alunos.txt, gravando
#  um nome por linha. Caso o arquivo já exista, ele deve 
# ser recriado do zero.

with open('alunos.txt', 'w', encoding='utf-8') as arquivo:
    for i in range(3):
        nome= input('Digite um nome: ')
        arquivo.write(nome+'\n')

# versão 2
lista = []
for i in range(3):
    nome = input('Digite um nome: ')
    lista.append(nome)

with open('aluno.txt','w', encoding='utf-8') as arquivo:
    arquivo.write(nome + '\n')