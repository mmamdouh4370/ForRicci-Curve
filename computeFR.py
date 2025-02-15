import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

G.add_weighted_edges_from([("S3A", "S2C", 1), ("S2C", "S1E", 2), ("S2C", "R1K", 1), ("S1E", "TC", 3), ("TC", "R1K", 4), ("R1K", "R2N", 4), 
                           ("R2N", "R3R", 1), ("R2N", "R3S", 5), ("S3B", "S2D", 3), ("S2D", "S1E", 2), ("S3G", "S2I", 1), ("S3H", "S2I", 2), 
                           ("S2I", "S1L", 4), ("S2I", "R1M", 5), ("S2I", "R1K", 3), ("S1L", "TC", 6), ("TC", "R1M", 3), ("R1M", "R2O", 2), ("R2O", "R3T", 4), 
                           ("R3S", "R3T", 2)])

for u, v in G.edges():
    w = G[u][v]['weight']
    sumU = sum((1 / ((w * G[x][u]['weight']) ** 0.5)) for x in G.predecessors(u) if x != v)
    sumV = sum((1 / ((w * G[v][y]['weight']) ** 0.5)) for y in G.successors(v) if y != u)
    G[u][v]['forman_ricci'] = (w * (1 / w - sumU)) + (w * (1 / w - sumV))

layout = {
    "S3A": (0, 3), "S2C": (1, 3), "S1E": (2, 2.5),
    "S3B": (0, 2), "S2D": (1, 2),
    "S3G": (0, 1), "S2I": (1, 0.5), "S1L": (2, 1),
    "S3H": (0, 0),
    
    "TC": (3, 1.5),
    
    "R1K": (4, 3), "R2N": (5, 3), "R3R": (6, 3), "R3S": (6, 2),
    "R1M": (4, 0), "R2O": (5, 0), "R3T": (6, 0)
}

nx.draw_networkx(G, layout, with_labels=True, node_size=1000)

edgeLabels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, layout, edge_labels=edgeLabels)

edgeLabelsFR = {(u, v): f"{data['forman_ricci']:.2f}" for u, v, data in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, layout, edge_labels=edgeLabelsFR, font_color='red', label_pos=0.3)


for u, v, data in G.edges(data=True):
    print(f"{u} to {v}, Edge weight = {data['weight']}, Forman Ricci Curvature = {data['forman_ricci']:.5f}")

plt.show()