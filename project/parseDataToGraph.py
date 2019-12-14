import os
import pandas as pd

path = "/media/lucas/My Home/repositorios/complex-networks-COS010/project/data/"

def getFiles():
    files = []
    print("path: ", path)
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if '.txt' in file:
                data = pd.read_csv(os.path.join(r, file), index_col="Date")[['Close']]
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

files = getFiles()

data = joinFiles(files)

data = removeNulls(data)

percentageReturns = data.pct_change()

corrMatrix = percentageReturns.corr()

print(corrMatrix)