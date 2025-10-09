import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Dados do gráfico
labels = ['Python', 'Java', 'C++', 'JavaScript', 'Ruby']
sizes = [40, 20, 10, 20, 10]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']
explode = (0.1, 0, 0, 0, 0)

# Criando a figura
fig, ax = plt.subplots()

# Criando o gráfico de pizza
ax.pie(sizes, explode=explode, labels=labels, colors=colors,
       autopct='%1.1f%%', startangle=140)
ax.axis('equal')
plt.title('Distribuição de Linguagens de Programação')

# Criando os quadradinhos coloridos (retângulos) para legenda
color_patches = [Rectangle((1, 1), 1, 1, facecolor=color) for color in colors]

# Adicionando a legenda no canto inferior direito
ax.legend(handles=color_patches, labels=labels,
          title="Linguagem", loc='center left',
          bbox_to_anchor=(0.8, 0.9), frameon=True)

fig.savefig('grafico_pizza1.svg')   # Salva como SVG

# Exibindo o gráfico
plt.show()
