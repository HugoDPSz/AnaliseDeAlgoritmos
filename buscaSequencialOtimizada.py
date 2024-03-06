import random

def insertionSort(lista):
    n = len(lista)
    for i in range(1, n):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j+1] = lista[j]
            j = j - 1
        lista[j+1] = chave

def buscaSequencial(lista, alvo, n):
    i = 0
    while alvo != lista[i] and i<n:
        if alvo < lista[i]:
            return None
        i = i + 1
    if alvo == lista[i]:
        return i
    else:
        return None

lista = random.sample(range(0,100000), 10000)
alvo = random.randint(0, 100000)
insertionSort(lista)
n = len(lista)
resultado = buscaSequencial(lista, alvo, n)
if resultado != None:
    print("O alvo está na posição ", resultado)
else:
    print("O alvo não está na lista")