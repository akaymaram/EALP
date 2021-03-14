import networkx as nx
from matplotlib import pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout

graph = nx.DiGraph()

Dict = {1: "sample sentece one.", 2: "sample sentence 2.", 3: "sample sentence three.", 4: "sample sentence four."}
graph.add_edges_from([(1, 2), (1, 3),
	(1, 4), (2, 3), (2, 4), (3, 4)], weight=10)
pos = nx.spring_layout(graph, seed=7)
# plt.tight_layout()
# nx.draw_networkx_nodes(graph, pos, node_size=700)
# nx.draw_networkx_edges(graph, pos, width=6)
nx.draw_networkx_edges(graph,pos,edge_color='b',alpha = 0.6)  # draws edges
nx.draw_networkx_edge_labels(graph,pos,edge_labels = nx.get_edge_attributes(graph,'weight'))
nx.draw_networkx(graph, pos,arrows=False)
plt.show()
# plt.savefig("g.png", format="PNG")
plt.clf()
print(Dict)



# from matplotlib import pyplot as plt
# import networkx as nx
# G = nx.Graph()
# G.add_edge(1,2)
# G.add_edge(2,3)
# # for v in G.nodes():
# #     G.node[v]['state']='X'
# # G.node[1]['state']='Y'
# # G.node[2]['state']='Y'

# for n in G.edges_iter():
#     G.edge[n[0]][n[1]]['state']='X'
# G.edge[2][3]['state']='Y'

# pos = nx.spring_layout(G)

# nx.draw(G, pos)
# node_labels = nx.get_node_attributes(G,'state')
# nx.draw_networkx_labels(G, pos, labels = node_labels)
# edge_labels = nx.get_edge_attributes(G,'state')
# nx.draw_networkx_edge_labels(G, pos, labels = edge_labels)
# plt.savefig('this.png')
# plt.show()