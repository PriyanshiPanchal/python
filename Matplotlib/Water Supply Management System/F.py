import matplotlib.pyplot as plt
import csv
import numpy as np
import pandas as pd

df = pd.read_csv("F.csv")
df.head()
df.plot.bar(x='Year',y=['Rural','Urban'])
plt.show()