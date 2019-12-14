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

def transformPercentageReturn(files):
    percentageReturn = []
    for file in files:
        percentageReturn.append(file.pct_change())
    return percentageReturn

files = getFiles()

percentageReturns = transformPercentageReturn(files)

data = joinFiles(files)

print(data)
