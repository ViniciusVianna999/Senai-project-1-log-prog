import random
print('Bem vindo ao jogo de adivinhação')
pontos = 0
for i in range(3):
    print(f'Essa é sua {i+1} rodada')
    numero_aleatorio = random.randint(1, 50)
    tentativas = 0 
    acertou = False  # variavel de controle
    
# enquanto tiver chances
while tentativas <= 5:
    palpite = int(input('Dê seu chute (1 à 50): '))

    # se acertou
    if palpite == numero_aleatorio:
        print('Você acertou')
        if tentativas == 1:
            pontos += 100 #acertou de primeira
        elif tentativas == 5:
            pontos += 10
        else:
            pontos += (100 - tentativas*25)
        break # para a execução do laço While

    # ajudas
    elif palpite <  numero_aleatorio:
        print('Tente um numero maior')
    
    elif palpite > numero_aleatorio:
        print('Tente um numero menor')


    tentativas += 1 #usou uma tentativa
if not acertou:
    print(f'Nessa rodada ({i+1}), você errou muito, gastou tudo')

if pontos >= 200:
    print(f'Sabe muito, faturou {pontos} pontos')
elif 100< pontos <200:
    print(f'Ate que tu sabe algo, {pontos} nessa ')
else:
    print(f'Tente de novo, ou não {pontos} nessa rodada1')
