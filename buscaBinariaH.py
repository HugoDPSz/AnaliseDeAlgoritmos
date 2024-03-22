import random
import time

def buscaBinaria(lista, alvo, inicio, fim):
    if inicio <= fim:
        teste = (inicio + fim) // 2
        if lista[teste] == alvo:
            return None
        if lista[teste] < alvo:
            return buscaBinaria(lista, alvo, teste + 1, fim)
        else:
            return buscaBinaria(lista, alvo, inicio, teste - 1)
    return None


inicio = 0
numInteracoes = 1000
tempoTotal = [0] * numInteracoes
tempoMedia = [0] * 16
tamanhos_vetor = [10**4, 10**5, 10**6, 10**7]

for tamanho in tamanhos_vetor:
    for j in range(16):
        lista = random.sample(range(0, tamanho), tamanho)
        alvo = random.randint(0, tamanho)
        lista.sort()  
        fim = len(lista)  
        for i in range(numInteracoes):
            inicioTempo = time.time()
            buscaSBinaria(lista, alvo, inicio, fim-1)  
            fimTempo = time.time()
            tempoTotal[i] = fimTempo - inicioTempo
        tempoMedia[j] = sum(tempoTotal) / numInteracoes
    mediaTotal = sum(tempoMedia)
    print("Tamanho do vetor: %d - Tempo de execução médio: %.10f segundos" % (tamanho, mediaTotal))  