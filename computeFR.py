import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

G.add_weighted_edges_from([("S3A", "S2C", 1), ("S2C", "S1E", 2), ("S2C", "R1K", 1), ("S1E", "TC", 3), ("TC", "R1K", 4), ("R1K", "R2N", 4), 
                           ("R2N", "R3R", 1), ("R2N", "R3S", 5), ("S3B", "S2D", 3), ("S2D", "S1E", 2), ("S3G", "S2I", 1), ("S3H", "S2I", 2), 
                           ("S2I", "S1L", 4), ("S2I", "R1M", 4), ("S1L", "TC", 6), ("TC", "R1M", 3), ("R1M", "R2O", 2), ("R2O", "R3T", 4), 
                           ("R3S", "R3T", 2)])

for u, v in G.edges():
    w = G[u][v]['weight']
    sumU = sum((1 / ((w * G[x][u]['weight']) ** 0.5)) for x in G.predecessors(u) if x != v)
    sumV = sum((1 / ((w * G[v][y]['weight']) ** 0.5)) for y in G.successors(v) if y != u)
    G[u][v]['forman_ricci'] = (w * (1 / w - sumU)) + (w * (1 / w - sumV))

layout = nx.spring_layout(G, seed=12) 
nx.draw_networkx(G, layout, with_labels=True)
edgeLabels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, layout, edge_labels=edgeLabels)

for u, v, data in G.edges(data=True):
    print(f"{u} to {v}, Edge weight = {data['weight']}, Forman Ricci Curvature = {data['forman_ricci']:.5f}")

plt.show()