import matplotlib.pyplot as plt


categorias = ['A', 'B', 'C', 'D']
valores = [40, 30, 55, 79]


plt.figure(num="Figura de Exemplo para Gráfico de Barras")
plt.bar(categorias, valores , color='skyblue')
plt.title('Gráfico de Barras')
plt.xlabel('Categorias')
plt.ylabel('Valores')


plt.show()

##