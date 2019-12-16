from graph_tool.all import *

g = load_graph("/media/lucas/My Home/repositorios/complex-networks-COS010/project/data/stocks.gt")

label = g.vp.label
for v in g.vertices():
    print(label[v])