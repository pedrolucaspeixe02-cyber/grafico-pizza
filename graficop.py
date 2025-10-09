import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Dados do gráfico
labels = ['Python', 'Java', 'C++', 'JavaScript', 'Ruby']
sizes = [40, 20, 10, 20, 10]
colors = ["#ff0000", "#0080ff", "#00ff00", "#f97c00", "#0000ff"]
explode = (0.1, 0, 0, 0, 0)

# Criando a figura
fig, ax = plt.subplots()

# Criando o gráfico de pizza
ax.pie(sizes, explode=explode, labels=labels, colors=colors,
       autopct='%1.1f%%', startangle=140)
ax.axis('equal')
plt.title('Distribuição de Linguagens de Programação')

# Ajustar a posição do eixo para mover o gráfico para a esquerda
box = ax.get_position()
ax.set_position([box.x0 - 0.1, box.y0, box.width, box.height])

# Criando os quadradinhos coloridos (retângulos) para legenda
color_patches = [Rectangle((0, 0), 1, 1, facecolor=color) for color in colors]

# Adicionando a legenda no canto inferior direito
ax.legend(handles=color_patches, labels=labels,
          title="Linguagem", loc='center left',
          bbox_to_anchor=(0.95, 0.5), frameon=True)

fig.savefig('grafico_pizza1.svg')   # Salva como SVG

# Exibindo o gráfico
plt.show()
