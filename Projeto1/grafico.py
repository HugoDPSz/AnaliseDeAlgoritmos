import matplotlib.pyplot as plt

tamanhos_binaria = []
tempos_binaria = []
tamanhos_sequencial = []
tempos_sequencial = []
tamanhos_sequencial_otimizada = []
tempos_sequencial_otimizada = []

def ler_arquivo(nome_arquivo, lista_tamanhos, lista_tempos):
    with open(nome_arquivo, "r") as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            partes = linha.split(" - ")
            if len(partes) == 2:
                tamanho = int(partes[0].split(": ")[1])
                tempo = float(partes[1].split(": ")[1].split(" segundos")[0])
                lista_tamanhos.append(tamanho)
                lista_tempos.append(tempo)

ler_arquivo("outputBuscaBinaria100.txt", tamanhos_binaria, tempos_binaria)
ler_arquivo("outputBuscaSequencial100.txt", tamanhos_sequencial, tempos_sequencial)
ler_arquivo("outputBuscaSequencialOtimizada100.txt", tamanhos_sequencial_otimizada, tempos_sequencial_otimizada)

tamanhos_binaria, tempos_binaria = zip(*sorted(zip(tamanhos_binaria, tempos_binaria)))
tamanhos_sequencial, tempos_sequencial = zip(*sorted(zip(tamanhos_sequencial, tempos_sequencial)))
tamanhos_sequencial_otimizada, tempos_sequencial_otimizada = zip(*sorted(zip(tamanhos_sequencial_otimizada, tempos_sequencial_otimizada)))

plt.figure(figsize=(10, 6))
plt.plot(tamanhos_binaria, tempos_binaria, marker='o', linestyle='-', color='b', label='Busca Binária')
plt.plot(tamanhos_sequencial, tempos_sequencial, marker='s', linestyle='-', color='g', label='Busca Sequencial')
plt.plot(tamanhos_sequencial_otimizada, tempos_sequencial_otimizada, marker='^', linestyle='-', color='r', label='Busca Sequencial Otimizada')

valores_y_log = [0.0001, 0.001, 0.01, 0.1, 1.0, 10]

plt.yticks(valores_y_log)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Tamanho do Vetor')
plt.ylabel('Tempo de Execução (segundos)')
plt.title('Comparação de Tempo de Execução: Busca Sequencial vs. Busca Binária vs. Busca Sequencial Otimizada')
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.show()