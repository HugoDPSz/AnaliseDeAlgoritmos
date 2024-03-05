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

def buscaBinaria(lista, alvo, inicio, fim):
    if inicio <= fim:
        teste = (inicio + fim)// 2
        if lista[teste] == alvo:
            return teste
        if lista[teste] < alvo:
            return buscaBinaria(lista, alvo, teste+1, fim)
        else:
            return buscaBinaria(lista, alvo, inicio, teste-1)
    return None

#main
lista = random.sample(range(0,1000000000), 10000000)
insertionSort(lista)
alvo = random.randint(0, 1000000000)
inicio = 0
fim = len(lista) - 1
resultado = buscaBinaria(lista, alvo, inicio, fim)
if resultado != None:
    print("O alvo está na posição {resultado}")
else:
    print("O alvo não está na lista")