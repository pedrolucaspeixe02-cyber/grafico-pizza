import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Dados do gráfico
labels = ['Python', 'Java', 'C++', 'JavaScript', 'Ruby']
sizes = [40, 20, 10, 20, 10]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']
explode = (0.1, 0, 0, 0, 0)

# Criando a figura
fig, ax = plt.subplots()

# Gráfico de pizza com "sombra" (efeito 3D)
ax.pie(sizes, explode=explode, labels=labels, colors=colors,
       autopct='%1.1f%%', startangle=140, shadow=True)
ax.axis('equal')
plt.title('Distribuição de Linguagens de Programação (Simulação 3D)')

# Quadrados coloridos para legenda
color_patches = [Rectangle((0, 0), 1, 1, facecolor=color) for color in colors]

# Legenda posicionada à direita
ax.legend(handles=color_patches, labels=labels,
          title="Linguagem", loc='center left',
          bbox_to_anchor=(1.05, 0.5), frameon=True)

plt.tight_layout()

fig.savefig('grafico_pizza2.svg')   # Salva como SVG

plt.show()
