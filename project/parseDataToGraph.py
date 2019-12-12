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
                files.append(pd.read_csv(os.path.join(r, file), index_col="Date"))
    return files

def transformPercentageReturn(files):
    for i in range(len(files)):
        files[i] = files[i].pct_change()

files = getFiles()

transformPercentageReturn(files)

print(files[0])