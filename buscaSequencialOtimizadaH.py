import random
import time

def buscaSequencial(lista, alvo, n):
    i = 0
    while alvo != lista[i] and i<n:
        if alvo < lista[i]:
            return None
        i = i + 1
    if alvo == lista[i]:
        return None
    else:
        return None


numInteracoes = 1000
tempoTotal = [0] * numInteracoes
tempoMedia = [0] * 16
tamanhos_vetor = [10**4, 10**5, 10**6, 10**7]

for tamanho in tamanhos_vetor:
    for j in range(16):
        lista = random.sample(range(0, tamanho), tamanho)
        alvo = random.randint(0, tamanho)
        lista.sort()  
        n = len(lista)  
        for i in range(numInteracoes):
            inicioTempo = time.time()
            buscaSequencial(lista, alvo, n)  
            fimTempo = time.time()
            tempoTotal[i] = fimTempo - inicioTempo
        tempoMedia[j] = sum(tempoTotal) / numInteracoes
    mediaTotal = sum(tempoMedia)
    print("Tamanho do vetor: %d - Tempo de execução médio: %.10f segundos" % (tamanho, mediaTotal))  