import matplotlib.pyplot as plt

# Dados de vendas mensais
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Maio', 'Jun', 
         'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
vendas = [2000, 2100, 2500, 2300, 2700, 3000, 2800, 2900, 3200, 3300, 3500, 4000]

# Criar o gráfico de linha
plt.figure(figsize=(10, 5))
plt.plot(meses, vendas, marker='o', linestyle='-', color='b')

# Adicionar título e rótulos aos eixos
plt.title('Vendas Mensais de uma Loja ao Longo de um Ano')
plt.xlabel('Meses')
plt.ylabel('Vendas (em unidades)')

# Mostrar o gráfico
plt.grid(True)
plt.show()
