from graph_tool.all import *

networkName = "com-youtube.ungraph"
f = open("/home/lucas/Downloads/"+networkName+".txt","r")

fl =f.readlines()

g = Graph(directed=False)

nodes = int(fl[2].replace("#","").split()[1])-1

g.add_vertex(nodes)
i = 0
for x in fl[4:]:
	v1, v2 = x.split()
	g.add_edge(v1, v2)
	i+=1
	if(i%100000==0):
		print(i)

g.save("tmp/"+networkName+".gt")

f.close