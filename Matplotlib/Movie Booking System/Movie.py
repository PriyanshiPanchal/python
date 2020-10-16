
from datetime import datetime
import matplotlib.pyplot as plt
import csv
import numpy as np
import pandas as pd

df = pd.read_csv("BookingData.csv")
# print(df)
df.head()

numFiles = []
pathName = os.getcwd()
fileNames = os.listdir(pathName)
for fileNames in fileNames:
    if fileNames.endswith(".csv"):
        numFiles.append(fileNames)

for i in numFiles:
    file = open(os.path.join(pathName, i), "rU")
    reader = csv.reader(file, delimiter=',')
    for column in reader:
        print(column[4])

