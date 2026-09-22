lista = []

carros = ['Ferrari F430 Spider', 'Monza Tubarão',
'Golf Sapão', 'Uno com Escada', 'Opala SS Beberrão',
'New Civic',]

# slice -> selecionar elementos de uma lista
dois_carros = carros[0:3] # seleciona do 0 até o 3, mas não inclui o 3
print(dois_carros)

# adicionar na lista(no final da lista)
carros.append('Celta Preto')
print(carros)
print(30*'-')

 #retira do fim da lista
# em python, aceita parametro(pode tirar de qualquer lugar da lista)
carros.pop()
print(carros)

# New Civic
carros[5]

# Fim da Lista - esse '-1' mostra a ultima posição
carros[-1]


# penultima
carros[-2] 

#  verificar o tipo
# print(type(carros))

# imprimir 1 elemento
# print(carros[4])

# imprimir a lista (como ela está)
# print(carros)

# imprimir elemento por elemento
# for carro in carros:
    # print(f'{carro}')

# for i in range(len(carros)):
    # print(f'{i+1} - {carros[i]}')

    # notas=[10, 9, 8, 9.5, 7, 4.5, 6]
    # for i in range(len(notas)):
    #     print(f'{i+1} - {notas[i]}')




# sopa = [0, 1.2, 'a', 'E, ai?', True
#['mais uma lista']]
# print(type(s), s) 

# lista para cadastro
# cadastro = ['Senai','eu@senai.br', '01/01/1900'
            # 'rua xavier, 417', '21 66666-6666'] 


