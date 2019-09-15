from graph_tool.all import *
import pprint
import numpy as np
import matplotlib.pyplot as plt
import sys

networkName = str(sys.argv[1])
tmpDir = "tmp/"

g = load_graph(tmpDir+networkName+".gt")

inDegrees = g.get_in_degrees(g.get_vertices())
outDegrees = g.get_out_degrees(g.get_vertices())

stats = {
	"degree": {
		"in" : {
			"mean": 	np.average(inDegrees),
			"std":		np.std(inDegrees),
			"max": 		np.amax(inDegrees),
			"min": 		np.amin(inDegrees),
			"median": 	np.median(inDegrees)
		},
		"out" : {
			"mean" : 	np.average(outDegrees),
			"std":		np.std(outDegrees),
			"max": 		np.amax(outDegrees),
			"min": 		np.amin(outDegrees),
			"median": 	np.median(outDegrees)
		}
	}
}



pp = pprint.PrettyPrinter(indent=4)
pp.pprint(stats)

plt.hist(outDegrees, bins=50)
plt.gca().set(title='Frequency Histogram', ylabel='Frequency');
plt.savefig(tmpDir+networkName+'outDegreesHistogram-.png')

plt.hist(inDegrees, bins=50)
plt.gca().set(title='Frequency Histogram', ylabel='Frequency');
plt.savefig(tmpDir+networkName+'inDegreesHistogram-.png')

f = open(tmpDir+networkName+"stats.txt","w+")
f.write(str(stats))
f.close()