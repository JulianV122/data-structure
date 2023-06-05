import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

def dijkstra(Grafo, salida):
    dist, prev = {}, {}
    result = []

    for vertice in Grafo:
        dist[vertice] = float("inf")
        prev[vertice] = None
    dist[salida] = 0

    vertice_visited = [vertice for vertice in Grafo]

    while vertice_visited:
        u = min(vertice_visited, key=dist.get)
        vertice_visited.remove(u)
        result.append(u)

        for vecino in Grafo[u]:
            if vecino in vertice_visited and dist[vecino] > dist[u] + Grafo[u][vecino]:
                dist[vecino] = dist[u] + Grafo[u][vecino]
                prev[vecino] = u

    return result, dist, prev

G.add_node("Armenia")
G.add_node("Barranquilla")
G.add_node("Cali")
G.add_node("Pereira")
G.add_node("Bogotá")
G.add_node("Medellín")
G.add_node("Neiva")
G.add_node("Santa Marta")

G.add_edge("Armenia","Barranquilla", weight = 4)
G.add_edge("Armenia","Cali", weight = 3)
G.add_edge("Barranquilla","Pereira", weight = 5)
G.add_edge("Cali","Barranquilla", weight = 2)
G.add_edge("Cali","Pereira", weight = 3)
G.add_edge("Cali","Bogotá", weight = 6)
G.add_edge("Pereira","Bogotá", weight = 5)
G.add_edge("Pereira","Neiva", weight = 1)
G.add_edge("Bogotá","Medellín", weight = 5)
G.add_edge("Medellín","Santa Marta", weight = 4)
G.add_edge("Neiva","Medellín", weight = 2)
G.add_edge("Neiva","Santa Marta", weight = 7)



grafo = {
    'Armenia': {'Barranquilla': 4, 'Cali': 3},
    'Barranquilla': {'Pereira': 5},
    'Cali': {'Barranquilla': 2, 'Pereira': 3, 'Bogotá': 6},
    'Pereira': {'Bogotá': 5, 'Neiva': 1},
    'Bogotá': {'Medellín': 5},
    'Medellín': {'Santa Marta': 4},
    'Neiva': {'Medellín': 2, 'Santa Marta': 7},
    'Santa Marta': {}
}


s, distancia, previos = dijkstra(grafo, 'Armenia')
print(f"{s=}")
print(f"{distancia=}")
#print(f"{previos=}")

nx.draw(G,with_labels=True)
plt.show()
