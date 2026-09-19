# Crie uma função que coloque qualquer texto no seguinte
#  padrão e o retorne:
# Tudo em minúscula.
# Sem espaços na frente ou atrás 
# (começando e finalizando o texto).

def limpar_texto(texto):
    novo_texo = texto.lower() #tudo em minúscula
    novo_texo = novo_texo.strip() #remove espaços no começo e no final da string
    return novo_texo

def limpar_texto_de_uma_vez(texto):
    return texto.strip().lower()
