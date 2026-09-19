# somar 2numeros
def somar(a, b):
    a = a + b #esse só existe dentro do escopo da função
    return a # isso faz ser uma função

a = 5 # esse 'a' aqui não é o mesmo 'a' que está dentro da função, são variáveis diferentes
b = 4
c = somar(b, a) # 4, 5 
print(c)
print(a)



# subtrair 2 numeros
def subtrair(a, b):
    """
    Essa função subtrai o 'a' de 'b' e retorna o valor
    """
    return a - b

# subtrair()

# saber se é impar
def impar(numero):
    """
    Essa função verifica se o número é impar
    """
    if not numero % 2 == 0:
        return True
    
    return False
def impar2(numero):
    return not numero % 2 == 0