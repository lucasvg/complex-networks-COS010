from graph_tool.all import *
import pprint
import numpy as np
import matplotlib.pyplot as plt
import sys

def vertexProperties2Json(g, iVertex):
	text = {}
	for prop in g.vertex_properties.keys():
		text[prop] = g.vertex_properties[prop][iVertex]
	return text

networkName = str(sys.argv[1])
tmpDir = "tmp/"

g = load_graph(tmpDir+networkName+".gt")

inDegrees = g.get_in_degrees(g.get_vertices())
outDegrees = g.get_out_degrees(g.get_vertices())

iInMax = np.argmax(inDegrees)
iInMin = np.argmin(inDegrees)
iOutMax = np.argmax(outDegrees)
iOutMin = np.argmin(outDegrees)

stats = {
	"degree": {
		"in" : {
			"mean": 	np.average(inDegrees),
			"std":		np.std(inDegrees),
			"max": {
				"degree": inDegrees[iInMax],
				"props": vertexProperties2Json(g, iInMax)
			},
			"min": 		{
				"degree": inDegrees[iInMin],
				"props": vertexProperties2Json(g, iInMin)
			},
			"median": 	np.median(inDegrees)
		},
		"out" : {
			"mean" : 	np.average(outDegrees),
			"std":		np.std(outDegrees),
			"max": {
				"degree": outDegrees[iOutMax],
				"props": vertexProperties2Json(g, iOutMax)
			},
			"min": 		{
				"degree": outDegrees[iOutMin],
				"props": vertexProperties2Json(g, iOutMin)
			},
			"median": 	np.median(outDegrees)
		}
	}
}



pp = pprint.PrettyPrinter(indent=4)
pp.pprint(stats)

plt.hist(outDegrees, bins=100)
plt.gca().set(title='Frequency Histogram', ylabel='Frequency');
plt.savefig(tmpDir+networkName+'outDegreesHistogram-.png')

plt.hist(inDegrees, bins=100)
plt.gca().set(title='Frequency Histogram', ylabel='Frequency');
plt.savefig(tmpDir+networkName+'inDegreesHistogram-.png')

f = open(tmpDir+networkName+"stats.txt","w+")
f.write(str(stats))
f.close()