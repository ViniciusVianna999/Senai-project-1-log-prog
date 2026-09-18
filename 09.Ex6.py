# usuario digita uma nota
# program verifica e só aceita se estiver
# entre 0 e 10, caso contrario, peça para
# digitar de novo

nota = float(input('Digite a nota:'))

while(nota < 0 or nota > 10):
    print(f'Voce digitou {nota}, mas ela deve estar entre 0 e 10.')
    nota = float(input('Digite a nota:'))

# while not(nota >= 0 and nota <= 10):
# pass

while True:
    if usuario == 0:
        # soma
        # qtd
        exit(0) # ou break