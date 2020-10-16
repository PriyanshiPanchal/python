import matplotlib.pyplot as plt
import pandas as pd
df =  pd.read_csv('H.csv')
region = df['Region']
total = df['Total(%)']
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#8c564b']  
plt.pie(total, labels=region, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.show()