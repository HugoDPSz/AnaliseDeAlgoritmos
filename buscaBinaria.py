import random

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


lista = random.sample(range(0,100000), 10000)
lista.sort
alvo = random.randint(0, 100000)
inicio = 0
fim = len(lista)
resultado = buscaBinaria(lista, alvo, inicio, fim)
if resultado is None:
    print("O alvo não está na lista")
else:
    print("O alvo está na posição ", resultado)