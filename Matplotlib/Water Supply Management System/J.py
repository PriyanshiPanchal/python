import matplotlib.pyplot as plt
import pandas as pd
df =  pd.read_csv('J.csv')

fig = plt.figure(figsize=(20,20), dpi=100)
ax1 = plt.subplot2grid((4,2),(0,0))
y = df['Year']
ep = df['Estimated Population']
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#8c564b']  
plt.pie(ep, labels=y, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Estimated Population', bbox={'facecolor':'0.8', 'pad':5})

ax1 = plt.subplot2grid((4,2),(0,1))
ga = df['Geographical Area']
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#8c564b']  
plt.pie(ga, labels=y, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Geographical Area', bbox={'facecolor':'0.8', 'pad':5})

ax1 = plt.subplot2grid((4,2),(1,0))
ra = df['Repoting Area']
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#8c564b']  
plt.pie(ra, labels=y, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Repoting Area', bbox={'facecolor':'0.8', 'pad':5})

ax1 = plt.subplot2grid((4,2),(1,1))
nsa = df['Net Sown Area']
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#8c564b']  
plt.pie(nsa, labels=y, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Net Sown Area', bbox={'facecolor':'0.8', 'pad':5})

ax1 = plt.subplot2grid((4,2),(2,0))
tca = df['Total Cultivable Area']
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#8c564b']  
plt.pie(tca, labels=y, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Total Cultivable Area', bbox={'facecolor':'0.8', 'pad':5})

ax1 = plt.subplot2grid((4,2),(2,1))
gsa = df['Gross Sown Area']
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#8c564b']  
plt.pie(gsa, labels=y, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Gross Sown Area', bbox={'facecolor':'0.8', 'pad':5})

ax1 = plt.subplot2grid((4,2),(3,0))
gia = df['Gross Irrigated Area']
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#8c564b']  
plt.pie(gia, labels=y, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Gross Irrigated Area', bbox={'facecolor':'0.8', 'pad':5})

ax1 = plt.subplot2grid((4,2),(3,1))
nia = df['Net Irrigated Area']
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#8c564b']  
plt.pie(nia, labels=y, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Net Irrigated Area', bbox={'facecolor':'0.8', 'pad':5})
plt.show()