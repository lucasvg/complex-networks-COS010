import os
import pandas as pd

path = os.getcwd() + "/data/"

def getFiles():
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if '.txt' in file:
                files.append(pd.read_csv(os.path.join(r, file)))
    return files

files = getFiles()

print(files)