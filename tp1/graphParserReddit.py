from graph_tool.all import *

networkName = "soc-redditHyperlinks-body"

def addVertex(subreddit, map):
	v = g.add_vertex()
	map[subreddit] = v
	g.vertex_properties["subreddit"][v] = subreddit

f = open("exampleGraphs/"+networkName+".tsv","r")

fl =f.readlines()

g = Graph(directed=True)
propSubreddit = g.new_vertex_property("string")
g.vertex_properties["subreddit"] = propSubreddit

subreddits = {}
for x in fl[1:]:
	values = x.split('\t')
	subreddit1 = values[0]
	subreddit2 = values[1]
	
	for subreddit in [subreddit1, subreddit2]:
		if subreddit not in subreddits:
			addVertex(subreddit, subreddits)

	g.add_edge(subreddits[subreddit1], subreddits[subreddit2])


g.save("tmp/"+networkName+".gt")

f.close