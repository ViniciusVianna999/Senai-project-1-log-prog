a = float(input('Digite o lado a: '))
b = float(input('Digite o lado b: '))
c = float(input('Digite o lado c: '))

if a + b > c and a + c > b and b + c > a:
    print('é um triangulo: ')

    # classificar o triangulo
    if a == b == c:
        print('triangulo equilátero')
    elif a == b or a == c or b == c:
        print('Trangulo é isósceles')
    else:
        print('Triangulo é Escaleno')
else: 
    print('Não é triangulo')

    # FEITO PELO PROFESSOR
    # 1 passo -> Receber 3 numeros
    # 2 passo -> Verificar a Soma dos Lados
    # 3 passo -> Se for Triangulo, classificar o tipo
    # 4 passo -> Erro se não for triangulo
    # lado_a = float(input('Digite o lado A: '))
    # lado_b = float(input('Digite o lado B: '))
    # lado_c = float(input('Digite o lado C: '))

    # condicao = ((lado_a + lado_b > lado_c) and
              #  (lado_a + lado_c > lado_b) and 
              #  (lado_a + lado_b > lado_c))
    
    # if condição:
        # if lado_a == lado_b == lado_c:
            # print('triangulo equilátero')

        # elif(lado_a != lado_b != lado_c:)
            # print('Triangulo é Escaleno')

        # elif (lado_a == lado_b or
        #       lado_a == lado_c or lado_b == lado_c):
            # print('Isosceles')
    # else: 
        # print('Não é um Triangulo')
        

    