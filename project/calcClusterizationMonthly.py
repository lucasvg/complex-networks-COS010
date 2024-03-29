from graph_tool.all import *
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt

path = "/media/lucas/My Home/repositorios/complex-networks-COS010/project/data/monthly/"
pathIndex = "/media/lucas/My Home/repositorios/complex-networks-COS010/project/data/^BVSP.txt"

def getAllGraphs():
    files = []
    print("path: ", path)
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if '.gt' in file:
                files.append(load_graph(os.path.join(r, file)))
    return files

def getIndexMonthly():
    df = pd.read_csv(pathIndex, index_col="Date", parse_dates=[0])[['Close']]
    return df.groupby(pd.Grouper(freq='M'), as_index=False).nth(-1)

gs = getAllGraphs()

clustMonthly = []
for g in gs:
    clustMonthly.append(global_clustering(g, weight=g.ep.weight)[0])

indexMonthly = getIndexMonthly()

indexMonthly['clusterization'] = clustMonthly

print(indexMonthly)
corrMatrix = indexMonthly.corr()
print(corrMatrix)
sns.heatmap(corrMatrix, 
        xticklabels=corrMatrix.columns,
        yticklabels=corrMatrix.columns)
plt.show()