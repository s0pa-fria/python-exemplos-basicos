import matplotlib.pyplot as plt

# Dados de participação de mercado
marcas = ['Marca A', 'Marca B', 'Marca C', 'Marca D', 'Marca E']
participacao = [35, 25, 20, 15, 5]

# Criar o gráfico de pizza
plt.figure(figsize=(8, 8))
plt.pie(participacao, labels=marcas, autopct='%1.1f%%', startangle=140, colors=['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'lightgrey'])

# Adicionar título
plt.title('Participação de Mercado das Marcas')

# Mostrar o gráfico
plt.show()
