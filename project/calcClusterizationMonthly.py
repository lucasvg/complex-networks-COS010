from graph_tool.all import *
import os

path = "/media/lucas/My Home/repositorios/complex-networks-COS010/project/data/monthly/"

def getAllGraphs():
    files = []
    print("path: ", path)
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if '.gt' in file:
                files.append(load_graph(os.path.join(r, file)))
    return files

gs = getAllGraphs()

clustMonthly = []
for g in gs:
    clustMonthly.append(global_clustering(g, weight=g.ep.weight))
print(clustMonthly)

