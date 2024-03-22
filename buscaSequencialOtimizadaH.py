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


tempoTotal = [0] * 100
tamanhos_vetor = [10**4, 10**5, 10**6, 10**7]

for tamanho in tamanhos_vetor:
    lista = random.sample(range(0, tamanho), tamanho)
    alvo = random.randint(0, tamanho)
    lista.sort()  
    n = len(lista)  
    for i in range(100):
        inicioTempo = time.time()
        buscaSequencial(lista, alvo, n)  
        fimTempo = time.time()
        tempoTotal[i] = fimTempo - inicioTempo
    tempoMedia = sum(tempoTotal) / 100
    print("Tamanho do vetor: %d - Tempo de execução médio: %.10f segundos" % (tamanho, tempoMedia))  