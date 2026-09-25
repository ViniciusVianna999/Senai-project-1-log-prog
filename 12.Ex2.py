# Construa um programa que peça ao usuário para digitar
#  oito números e os guarde em um vetor.
#  Depois, o programa deve pedir um número adicional
#  e informar se esse número está presente no vetor.
#  Se estiver, informe em qual posição (índice)
#  ele foi encontrado pela primeira vez.


lista = []

for i in range(0, 8):
    numero = int(input('Digite um numero: '))
    lista.append(numero)

# pegar o numero a ser procurado
meu_valor = int(input('Digite um numero: '))

# v1 -> usar o operador 'in'
if meu_valor in lista:
    print(f'Esta na lista, na posição: {lista.index(meu_valor)}')
else:
    print('Não esta na lista')
    
# V2 -> percorrer a lista
