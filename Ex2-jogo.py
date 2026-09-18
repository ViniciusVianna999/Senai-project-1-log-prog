import random
# definir a pontuação total
pontuação_total = 0

# definir o número de rodadas
for rodada in range(1, 4):
    numero_secreto = random.randint(0, 50)
    tentativa = 1
 

    print(f'rodada {rodada} de 3')
    # definir o número de tentativas
    while tentativa <= 5:
        chute = int(input('Digite um número entre 0 e 50: '))
        #  verificar se o chute está dentro do intervalo permitido
        if chute < 0 or chute > 50:
            print('Você deve digitar um número entre 0 e 50!')
            pass
        #  verificar se o chute é igual ao número secreto
        if chute == numero_secreto:
            print(f'Parabéns! Você acertou o número secreto {numero_secreto} na tentativa {tentativa}!')
            pontuação_total += 100 - (tentativa - 1) *20
            acertou = True
            break
        else:
            if chute < numero_secreto:
                print('O número secreto é maior.')
            else:
                print('O número secreto é menor.')
        

        tentativa += 1
    # verificar se o jogador não acertou o número secreto após todas as tentativas
    if not acertou:
        print(f'Você não acertou o número secreto {numero_secreto}.')
        print(f'Pontuação total: {pontuação_total}')


print(f'Pontuação total: {pontuação_total}')
