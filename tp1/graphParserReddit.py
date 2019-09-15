from graph_tool.all import *

networkName = "soc-redditHyperlinks-body"

def addVertex(id, map):
	v = g.add_vertex()
	map[id] = v

f = open("exampleGraphs/"+networkName+".tsv","r")

fl =f.readlines()

g = Graph(directed=True)

posts = {}

for x in fl:
	values = x.split('\t')
	post1 = values[0]
	post2 = values[1]
	
	for post in [post1, post2]:
		if post not in posts:
			addVertex(post, posts)

	g.add_edge(posts[post1], posts[post2])


g.save("tmp/"+networkName+".gt")

f.close