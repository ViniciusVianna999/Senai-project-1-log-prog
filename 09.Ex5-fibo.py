
anterior = 0
atual = 1

proximo = anterior + atual # 1
print(anterior)
print(atual)
print(proximo)
while (proximo <= 2000):
    anterior = atual
    atual = proximo
    proximo = anterior + atual
    print(proximo)







# trocando b por a

a = 10
b = 2

a, b = b, a