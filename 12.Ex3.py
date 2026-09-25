notas = []
for i in range(0, 6):
    nota = float(input('Digite a nota: '))
    notas.append(nota)

# media 
media = sum(notas)/len(notas)

# saber quem esta acima da media
# v1 - Pythones
acima_media = [nota for nota in notas if nota > media]

print(f'Qtd notas acima da média: {len(acima_media)} ')
for nota in acima_media:
    print(nota)

# v2 -> 'normal'
acima_media = []
for nota in notas:
    if nota > media:
        acima_media.append(nota)
