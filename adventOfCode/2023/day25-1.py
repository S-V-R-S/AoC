import networkx as nx
import matplotlib.pyplot as plt

f = open("advent code 2023\\input25.txt","r")
lignes = f.readlines()
f.close()



G = nx.Graph()
for l in lignes:
    n1, ns = l.strip().split(':')
    
    for n in ns.strip().split(" "):
        G.add_edge(n1, n)

# # nx.draw(G, with_labels=True)
# # plt.show()

# https://networkx.org/documentation/latest/reference/algorithms/generated/networkx.algorithms.connectivity.cuts.minimum_edge_cut.html#networkx.algorithms.connectivity.cuts.minimum_edge_cut
noeudsAEnlever = nx.minimum_edge_cut(G)
G.remove_edges_from(noeudsAEnlever)

# https://networkx.org/documentation/latest/tutorial.html#analyzing-graphs
graphes = list(nx.connected_components(G)) 
print(len(graphes[0])*len(graphes[1]))
