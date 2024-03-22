import subprocess

nome_arquivo_saida = "outputBuscaSequencial1000.txt"

comando_pypy = "python3 buscaSequencialH.py"

with open(nome_arquivo_saida, "w") as arquivo_saida:
    processo = subprocess.Popen(comando_pypy, shell=True, stdout=subprocess.PIPE)
    output, _ = processo.communicate()
    arquivo_saida.write(output.decode())  # Escreve a saída no arquivo

print(f"A saída foi salva em '{nome_arquivo_saida}'.")