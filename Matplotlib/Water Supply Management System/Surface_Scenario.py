import matplotlib.pyplot as plt

fig = plt.figure(figsize=(5,5), dpi=160)
ax1 = plt.subplot2grid((2,4),(0,0))
y = 'India','Gujarat'
ga = [3065000, 196024]
colors = ['#1f77b4', '#ff7f0e']  
plt.pie(ga, labels=y, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Geographical Area', bbox={'facecolor':'0.8', 'pad':5})

ax1 = plt.subplot2grid((2,4),(1,0))
y = 'India','Gujarat'
p = [121.01, 6.03]
colors = ['#1f77b4', '#ff7f0e']  
plt.pie(p, labels=y, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Population', bbox={'facecolor':'0.8', 'pad':5})

ax1 = plt.subplot2grid((2,4),(1,1))
y = 'India','Gujarat'
wa = [1869000, 38000]
colors = ['#1f77b4', '#ff7f0e']  
plt.pie(p, labels=y, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Water Availability', bbox={'facecolor':'0.8', 'pad':5})
plt.show()