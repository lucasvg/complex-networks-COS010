from graph_tool.all import *

g = load_graph("/media/lucas/My Home/repositorios/complex-networks-COS010/project/data/stocks.gt")

print(g.vp.label[g.vertex(0)])
for i in range(g.num_vertices()):
    print(g.vp.label[g.vertex(i)])
    print(g.ep.weight[g.edge(i, 0)])
