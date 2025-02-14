import matplotlib.pyplot as plt # type: ignore

# Dados
anos = [1650, 1960, 2000, 2020]
populacao = [300, 3000, 6000, 12000]  # Em milhões de habitantes

# Criando o gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(anos, populacao, color='skyblue')

# Adicionando título e rótulos
plt.title('Crescimento Populacional Mundial', fontsize=16)
plt.xlabel('Ano', fontsize=14)
plt.ylabel('População (milhões de habitantes)', fontsize=14)

# Ajustando os rótulos do eixo Y para facilitar a leitura
plt.yticks(range(0, 13000, 1000))

# Exibindo o gráfico
plt.show()