import networkx as nx
import matplotlib.pyplot as plt

# G va a ser la red de grafos
G = nx.Graph()

# Agregamos nodos al grafo
G.add_node("Yaneth")
G.add_node("Juan")
G.add_node("Alberto")
G.add_node("Lola Mento")
G.add_node("Marco de la Puerta")

# Agregamos las aristas entre los nodos
G.add_edge("Yaneth", "Juan", weight=3)
G.add_edge("Lola Mento", "Alberto", weight=14)
G.add_edge("Juan", "Lola Mento", weight=2)
G.add_edge("Yaneth", "Marco de la Puerta", weight=11) 
# Agregar varias aristas de una sola vez
G.add_edges_from(
    [("Yaneth", "Alberto"), ("Juan", "Marco de la Puerta"), ("Juan", "Lola Mento"),("Yaneth", "Marco de la Puerta")])

values = {("Yaneth", "Alberto"): 3,
          ("Juan", "Marco de la Puerta"): 14,
          ("Juan", "Lola Mento"): 2,
          ("Yaneth", "Marco de la Puerta"): 11
          }
# Dibujamos el grafo
pos = nx.spring_layout(G)
nx.draw(G, with_labels=True)
nx.draw_networkx_edge_labels(G, pos, edge_labels=values, label_pos=0.5, font_size=10, font_color='k', font_family='sans-serif', font_weight='normal', alpha=None, bbox=None, horizontalalignment='center', verticalalignment='center', ax=None, rotate=True, clip_on=True)

plt.show()