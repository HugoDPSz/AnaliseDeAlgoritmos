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
tempoTotal = [0] * 100
tamanhos_vetor = [10**4, 10**5, 10**6, 10**7]

for tamanho in tamanhos_vetor:
    lista = random.sample(range(0, tamanho), tamanho)
    alvo = random.randint(0, tamanho)
    lista.sort()  
    fim = len(lista)  
    for i in range(100):
        inicioTempo = time.time()
        buscaBinaria(lista, alvo, inicio, fim - 1)  
        fimTempo = time.time()
        tempoTotal[i] = fimTempo - inicioTempo
    tempoMedia = sum(tempoTotal) / 100
    print("Tamanho do vetor: %d - Tempo de execução médio: %.10f segundos" % (tamanho, tempoMedia))  