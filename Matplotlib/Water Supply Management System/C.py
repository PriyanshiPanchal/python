import matplotlib.pyplot as plt
import csv
import numpy as np
import pandas as pd

df = pd.read_csv("C.csv")
df.head()
df['Percentage'] = df['Percentage'].fillna(df['Percentage'].mean())
df.plot.bar(x='Year',y='Percentage')
plt.show()