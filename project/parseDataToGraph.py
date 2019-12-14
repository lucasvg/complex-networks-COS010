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

def transformPercentageReturn(files):
    percentageReturn = []
    for file in files:
        percentageReturn.append(file.pct_change())
    return percentageReturn

files = getFiles()

percentageReturns = transformPercentageReturn(files)

print(percentageReturns[0])