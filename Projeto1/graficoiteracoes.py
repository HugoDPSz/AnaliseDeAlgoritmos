import matplotlib.pyplot as plt

tempo10000_sequencial = [1.60408e-05, 3.17264e-05, 2.92301e-05, 1.94454e-05, 3.24035e-05, 2.91491e-05, 2.36201e-05, 3.11065e-05, 3.26443e-05, 2.63214e-05, 2.79212e-05, 3.14951e-05, 3.35813e-05, 2.90251e-05, 3.44825e-05, 1.71566e-05]
tempo100000_sequencial = [7.04288e-05, 8.95357e-05, 0.0001593733, 0.0002238321, 0.0002352762, 0.0001363111, 0.0002291369, 0.0002159595, 0.0001065516, 0.0001490903, 0.0001036453, 0.0002049613, 0.0001728106, 0.0002027798, 0.0001486945, 0.0001506281]
tempo1000000_sequencial = [0.0027830672, 0.0008738208, 0.0006426597, 0.0006722975, 0.0004967737, 0.0026115775, 0.0019229555, 0.0004291034, 0.0015397763, 0.0021139693, 0.0016133475, 0.0009698558, 8.68225e-05, 0.0021424985, 0.0014654827, 0.0017221117]
tempo10000000_sequencial = [0.0061245036, 0.0197366214, 0.004552598, 0.0031844711, 0.0190922642, 0.020276587, 0.0257683897, 0.0248922753, 0.0230502892, 0.0010079527, 0.0126842427, 0.0070319223, 0.0189627361, 0.0161594915, 0.0184339356, 0.0119378781]

tempo10000_sequencial_sum = sum(tempo10000_sequencial)
tempo100000_sequencial_sum = sum(tempo100000_sequencial)
tempo1000000_sequencial_sum = sum(tempo1000000_sequencial)
tempo10000000_sequencial_sum = sum(tempo10000000_sequencial)

resultado10000_sequencial = tempo10000_sequencial_sum / 16
resultado100000_sequencial = tempo100000_sequencial_sum / 16
resultado1000000_sequencial = tempo1000000_sequencial_sum / 16
resultado10000000_sequencial = tempo10000000_sequencial_sum / 16

x_sequencial = [10000, 100000, 1000000, 10000000]
y_sequencial = [resultado10000_sequencial, resultado100000_sequencial, resultado1000000_sequencial, resultado10000000_sequencial]

###########################################################################################################################################
# Tempos de execução médios da busca binária
tempo10000_binaria = [0.0000138497, 0.0000130963, 0.0000120568, 0.0000105381, 0.0000158787, 0.0000123405, 0.0000198317, 0.0000127387, 0.0000110626, 0.0000122499, 0.0000094485, 0.0000134468, 0.0000135922, 0.0000119567, 0.0000132895]
tempo100000_binaria = [0.0001236248, 0.0001130271, 0.0001057434, 0.0000948715, 0.0001143479, 0.0000893378, 0.0001383591, 0.0001315141, 0.0001185608, 0.0001422882, 0.0001251793, 0.0000985003, 0.0001296973, 0.0001313663, 0.0001425505]
tempo1000000_binaria = [0.0001304483, 0.0001151967, 0.0001303363, 0.0001361513, 0.0001140785, 0.0001218414, 0.0001305652, 0.0001140022, 0.0000806355, 0.0003314352, 0.0000269461, 0.0001345682, 0.0001102805, 0.0001341844, 0.0001162481]
tempo10000000_binaria = [0.0000560474, 0.0000761652, 0.0000672007, 0.0000626588, 0.0000667024, 0.0000656962, 0.0000662756, 0.0000674438, 0.0000719833, 0.0000639367, 0.0000724936, 0.0000602627, 0.0000719738, 0.0000671179, 0.0000638986]

# Calculando os resultados médios
resultado10000_binaria = sum(tempo10000_binaria) / len(tempo10000_binaria)
resultado100000_binaria = sum(tempo100000_binaria) / len(tempo100000_binaria)
resultado1000000_binaria = sum(tempo1000000_binaria) / len(tempo1000000_binaria)
resultado10000000_binaria = sum(tempo10000000_binaria) / len(tempo10000000_binaria)

x_binaria = [10000, 100000, 1000000, 10000000]
y_binaria = [resultado10000_binaria, resultado100000_binaria, resultado1000000_binaria, resultado10000000_binaria]

tempo10000_sequencialOtimizada = [0.0000320458, 0.0000358748, 0.0000380659, 0.0000259829, 0.0000295997, 0.0000188613, 0.0000321460, 0.0000335956, 0.0000239158, 0.0000238323, 0.0000195265, 0.0000195265, 0.0000239158, 0.0000238323, 0.0000195265, 0.0000195265]
tempo100000_sequencialOtimizada = [0.0001538897, 0.0000557590, 0.0000499511, 0.0000649858, 0.0001851726, 0.0001807284, 0.0001157475, 0.0002178812, 0.0000215435, 0.0000338173, 0.0001355147, 0.0000246334, 0.0000271630, 0.0001274562, 0.0000271630, 0.0001274562]
tempo1000000_sequencialOtimizada = [0.0013524604, 0.0007743502, 0.0016464615, 0.0005175352, 0.0017769504, 0.0015239859, 0.0022556067, 0.0008100772, 0.0019620681, 0.0022556067, 0.0021320271, 0.0018901277, 0.0023589492, 0.0019620681, 0.0016464615, 0.0021320271]
tempo10000000_sequencialOtimizada = [0.0159094930, 0.0095360565, 0.0183900595, 0.0082526159, 0.0167560267, 0.0167560267, 0.0178434777, 0.0185504532, 0.0174282718, 0.0167560267, 0.0213794899, 0.0195290422, 0.0213794899, 0.0195290422, 0.0213794899, 0.0195290422]

# Calculando os resultados médios
resultado10000_sequencialOtimizada = sum(tempo10000_sequencialOtimizada) / len(tempo10000_sequencialOtimizada)
resultado100000_sequencialOtimizada = sum(tempo100000_sequencialOtimizada) / len(tempo100000_sequencialOtimizada)
resultado1000000_sequencialOtimizada = sum(tempo1000000_sequencialOtimizada) / len(tempo1000000_sequencialOtimizada)
resultado10000000_sequencialOtimizada = sum(tempo10000000_sequencialOtimizada) / len(tempo10000000_sequencialOtimizada)

x_sequencialOtimizada = [10000, 100000, 1000000, 10000000]
y_sequencialOtimizada = [resultado10000_sequencialOtimizada, resultado100000_sequencialOtimizada, resultado1000000_sequencialOtimizada, resultado10000000_sequencialOtimizada]


# Plotando os dados
plt.plot(x_sequencial, y_sequencial, marker='o', label='Busca Sequencial')
plt.plot(x_binaria, y_binaria, marker='s', label='Busca Binária')
plt.plot(x_sequencialOtimizada, y_sequencialOtimizada, marker='^', label='Busca Sequencial Otimizada')

# Adicionando rótulos e título
plt.xlabel('Tamanho da Lista')
plt.ylabel('Tempo Médio (s)')
plt.title('Comparação de Tempo de Execução: Busca Sequencial vs. Busca Binária vs. Busca Sequencial Otimizada')

# Adicionando legenda
plt.legend()

# Exibindo o gráfico
plt.grid(True)
plt.xscale('log')
plt.yscale('log')
plt.show()



#python3 graficoiteracoes.py
