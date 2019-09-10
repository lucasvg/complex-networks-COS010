from graph_tool.all import *

networkName = "Amazon0302"
f = open("exampleGraphs/"+networkName+".txt","r")

fl =f.readlines()

g = Graph(directed=True)

nodes = int(fl[2].replace("#","").split()[1])-1

g.add_vertex(nodes)

for x in fl[4:]:
	v1, v2 = x.split()
	g.add_edge(v1, v2)

g.save("tmp/"+networkName+".gt")

f.close