from graph_tool.all import *
import pprint
import numpy as np

networkName = "Amazon0302"
tmpDir = "tmp/"

g = load_graph(tmpDir+networkName+".gt")

stats = {
	"degree": {
		"in" : {
			"mean" : vertex_average(g, "in"),
		},
		"out" : {
			"mean" : vertex_average(g, "out"),
		}
	}
}

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(stats)
