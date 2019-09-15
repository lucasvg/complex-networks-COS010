from graph_tool.all import *

networkName = "web-Google"

def addVertex(label, map):
	v = g.add_vertex()
	map[label] = v
	g.vertex_properties["label"][v] = label

f = open("exampleGraphs/"+networkName+".txt","r")

fl =f.readlines()

g = Graph(directed=True)
label = g.new_vertex_property("string")
g.vertex_properties["label"] = label

labels = {}
for x in fl[4:]:
	values = x.split()
	label1 = values[0]
	label2 = values[1]
	
	for label in [label1, label2]:
		if label not in labels:
			addVertex(label, labels)

	g.add_edge(labels[label1], labels[label2])


g.save("tmp/"+networkName+".gt")

f.close