import matplotlib.pyplot as plt
import csv
import numpy as np
import pandas as pd

df = pd.read_csv("B-Water.csv")
df.head()
df.plot.bar(x='Type',y=['Village','Towns'])
plt.show()