import matplotlib.pyplot as plt
import csv
import numpy as np
import pandas as pd

df = pd.read_csv("E.csv")
df.head()
df.plot.bar(x='Year',y=['Expected Supply','Supplied'])
z = df.groupby('Type')
z.plot.bar(stacked=True)
plt.show()