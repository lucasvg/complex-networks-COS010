from graph_tool.all import *

g = load_graph("/media/lucas/My Home/repositorios/complex-networks-COS010/project/data/stocks.gt")

print(global_clustering(g, weight=None))
print(global_clustering(g, weight=g.ep.weight))