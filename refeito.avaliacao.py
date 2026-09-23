nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2)/2

if media < 6: 
    print('aluno reprovado')
else:
    print('aluno aprovado')

# feito por mim
if media < 6 :
    print(f'Reprovado com média: {media}')
else: 
    print(f'Aprovado com média: {media}')

