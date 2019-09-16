from graph_tool.all import *
import pprint
import numpy as np
import matplotlib.pyplot as plt
import sys
from scipy import stats
import json

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
				"degree": inDegrees[iInMax]
			},
			"min": 		{
				"degree": inDegrees[iInMin]
			},
			"median": 	np.median(inDegrees),
			"mode": (lambda x: {"val": x[0][0], "count": x[1][0]})(stats.mode(inDegrees))
		},
		"out" : {
			"mean" : 	np.average(outDegrees),
			"std":		np.std(outDegrees),
			"max": {
				"degree": outDegrees[iOutMax]
			},
			"min": 		{
				"degree": outDegrees[iOutMin]
			},
			"median": 	np.median(outDegrees),
			"mode": (lambda x: {"val": x[0][0], "count": x[1][0]})(stats.mode(outDegrees))
		}
	}
}
if g.vertex_properties.keys():
	stats["degree"]["in"]["max"]['props'] = vertexProperties2Json(g, iInMax)
	stats["degree"]["in"]["min"]['props'] = vertexProperties2Json(g, iInMin)
	stats["degree"]["out"]["max"]['props'] = vertexProperties2Json(g, iOutMax)
	stats["degree"]["out"]["min"]['props'] = vertexProperties2Json(g, iOutMin)

comp, hist, is_attractor = label_components(g, directed=True, attractors=True)

stats['components'] = {"comp": str(comp), "hist": str(hist), "is_attractor": str(is_attractor)}

plt.figure()
plt.hist(comp.get_array(), bins=10)
plt.gca().set(title='Connected Components', ylabel='Frequency')
plt.savefig(tmpDir+networkName+'ConnectedComponentsHistogram-.png')

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(stats)

plt.figure()
plt.hist(outDegrees, bins=40)
plt.gca().set(title='outDegree Frequency Histogram', ylabel='Frequency')
plt.savefig(tmpDir+networkName+'outDegreesHistogram-.png')

plt.figure()
plt.hist(inDegrees, bins=50)
plt.gca().set(title='inDegrees Frequency Histogram', ylabel='Frequency')
plt.savefig(tmpDir+networkName+'inDegreesHistogram-.png')

f = open(tmpDir+networkName+"stats.txt","w+")
f.write(str(stats).replace("'", "\""))
f.close()