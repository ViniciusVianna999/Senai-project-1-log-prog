a = int(input('digite um número:'))
b = int(input('digite um número:'))

if a > b:
    a, b = b, a

soma = 0
for i in range(a, b + 1):
    if i % 2 != 0:
        soma += i
       
print(f"Soma dos números ímpares de [{a},{b}]: {soma}")
