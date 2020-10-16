import matplotlib.pyplot as plt
import csv
import numpy as np
import pandas as pd

df = pd.read_csv("D.csv")
df.head()
df.plot.bar(x='Condition',y=['Before','After'])
plt.show()