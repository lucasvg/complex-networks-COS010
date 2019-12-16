import os
import pandas as pd
from graph_tool.all import *

path = "/media/lucas/My Home/repositorios/complex-networks-COS010/project/data/"

def getFiles():
    files = []
    print("path: ", path)
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if '.txt' in file:
                data = pd.read_csv(os.path.join(r, file), index_col="Date", parse_dates=[0])[['Close']]
                files.append(data.add_prefix(file.replace('.txt', '')))
    return files

def joinFiles(files):
    df = files[0]
    for i in range(1, len(files)):
        df = df.join(files[i], lsuffix='', rsuffix='')
    return df

def removeNulls(data):
    totalNulls = data.isnull().sum()
    totalNulls = totalNulls[totalNulls>0]
    columns = totalNulls.index.array
    print(len(columns), ' columns removed due to null values!')
    return data.drop(columns=columns)

def splitMonthly(df):
    return df.groupby(pd.Grouper(freq='M'))

def calcCorrMonthly(percentagesMonthly):
    corr = []
    for name, p in percentageReturnsMonthly:
        corr.append(p.corr())
    return corr

def createGraph(data):
    graph = Graph(directed=False)
    stocks = data.columns.array
    
    graph.add_vertex(len(stocks))
    return graph

def createsPropLabel(graph, data):
    propLabel = g.new_vertex_property("string")
    graph.vertex_properties['label'] = propLabel
    stocks = data.columns.array
    stocks  = [x.replace('Close', '') for x in stocks]
    i = 0
    for v in graph.vertices():
        graph.vp.label[v] = stocks[i]
        i+=1

def loadsEdgesAndWeights(graph, corrMatrix):
    weights = graph.new_edge_property("float")
    graph.edge_properties['weight'] = weights
    matrix = corrMatrix.values
    cols = rows = len(matrix)
    for i in range(cols):
        for j in range(rows):
            graph.add_edge(graph.vertex(i), graph.vertex(j))
            graph.ep.weight[graph.edge(i, j)] = matrix[i][j]

files = getFiles()

data = joinFiles(files)

data = removeNulls(data)

percentageReturns = data.pct_change()

percentageReturnsMonthly = splitMonthly(percentageReturns)

corrMatrices = calcCorrMonthly(percentageReturnsMonthly)

for i in range(len(corrMatrices)):
    g = createGraph(data)
    createsPropLabel(g, data)
    loadsEdgesAndWeights(g, corrMatrices[i])
    g.save(path + "/monthly/"+str(i)+".gt")
