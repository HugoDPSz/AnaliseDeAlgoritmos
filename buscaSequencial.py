import random

def buscaSequencial(lista, alvo, n):
    i = 0
    while alvo != lista[i] and i<n:
        i = i + 1
    if alvo == lista[i]:
        return i
    else:
        return None


lista = random.sample(range(0,100000), 10000)
alvo = random.randint(0, 100000)
n = len(lista)
resultado = buscaSequencial(lista, alvo, n)
if resultado is None:
    print("O alvo não está na lista")
else:
    print("O alvo está na posição ", resultado)