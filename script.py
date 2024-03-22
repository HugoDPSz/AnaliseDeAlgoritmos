import subprocess

num_execucoes = 16

nome_arquivo_saida = "outputBuscaSequencial.txt"

comando_pypy = "pypy buscaSequencialH.py"

with open(nome_arquivo_saida, "w") as arquivo_saida:
    for _ in range(num_execucoes):
        processo = subprocess.Popen(comando_pypy, shell=True, stdout=subprocess.PIPE)
        output, _ = processo.communicate()
        arquivo_saida.write(output.decode())  # Escreve a saída no arquivo

print(f"A saída foi salva em '{nome_arquivo_saida}'.")